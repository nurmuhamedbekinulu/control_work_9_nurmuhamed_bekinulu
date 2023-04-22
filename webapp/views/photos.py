from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, FormView

from webapp.models import Photo, Favorite
from webapp.forms import PhotoForm, FavoriteForm


class PhotoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'photo_create.html'
    model = Photo
    form_class = PhotoForm
    success_message = 'Фото добавлено'

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class PhotoDetail(DetailView):
    template_name = 'photo.html'
    model = Photo


class GroupPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'manager']).exists()


class PhotoDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'photo_confirm_delete.html'
    model = Photo
    success_url = reverse_lazy('index')
    success_message = 'Фотография удалена'


class PhotoUpdateView(GroupPermissionMixin, LoginRequiredMixin, UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo
    success_message = 'Фотография обновлена'

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class FavoriteView(LoginRequiredMixin, FormView):
    form_class = FavoriteForm

    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            note = form.cleaned_data.get('note')
            user = request.user
            if not Favorite.objects.filter(user=user, photo=photo).exists():
                Favorite.objects.create(user=user, photo=photo, note=note)
                messages.success(request, 'Фото было добавлено в избранное')
        return redirect('index')

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, FormView

from webapp.models import Photo, Favorite
# from webapp.forms import ArticleForm, FavoriteForm


# class ArticleCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
#     template_name = 'article_create.html'
#     model = Article
#     form_class = ArticleForm
#     success_message = 'Статья создана'

#     def get_success_url(self):
#         return reverse('article_detail', kwargs={'pk': self.object.pk})


class PhotoDetail(DetailView):
    template_name = 'photo.html'
    model = Photo


# class GroupPermissionMixin(UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.groups.filter(name__in=['admin', 'manager']).exists()


# class ArticleUpdateView(GroupPermissionMixin, LoginRequiredMixin, UpdateView):
#     template_name = 'article_update.html'
#     form_class = ArticleForm
#     model = Article
#     success_message = 'Статья обновлена'

#     def get_success_url(self):
#         return reverse('article_detail', kwargs={'pk': self.object.pk})


# class ArticleDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
#     template_name = 'article_confirm_delete.html'
#     model = Article
#     success_url = reverse_lazy('index')
#     success_message = 'Статья удалена'


# class FavoriteView(LoginRequiredMixin, FormView):
#     form_class = FavoriteForm

#     def post(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs.get('pk'))
#         form = self.get_form_class()(request.POST)
#         if form.is_valid():
#             note = form.cleaned_data.get('note')
#             user = request.user
#             if not Favorite.objects.filter(user=user, article=article).exists():
#                 Favorite.objects.create(user=user, article=article, note=note)
#                 messages.success(request, 'Статья была добавлена в избранное')
#         return redirect('index')

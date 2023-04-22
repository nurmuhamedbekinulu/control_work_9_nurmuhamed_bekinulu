from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import RedirectView, ListView

from webapp.forms import SearchForm, PhotoForm
from webapp.models import Photo


class IndexView(ListView):
    pass
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('created_at',)
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(caption__icontains=self.search_value) | Q(author__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    # def get_context_data(self, **kwargs):
    #     if 'form' not in kwargs:
    #         kwargs['form'] = self.get_photo_form()
    #     return super().get_context_data(**kwargs)

    # def get_photo_form(self):
    #     form_kwargs = {'instance': self.object.photo}
    #     if self.request.method == 'POST':
    #         form_kwargs['data'] = self.request.POST
    #         form_kwargs['files'] = self.request.FILES
    #     return PhotoForm(**form_kwargs)



class IndexRedirectView(RedirectView):
    pattern_name = 'index'

from django.urls import path


from webapp.views.base import IndexView, IndexRedirectView

urlpatterns =[
    path("", IndexView.as_view(), name='index'),
    path("article/", IndexRedirectView.as_view(), name='articles_index_redirect'),
]


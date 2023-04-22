from django.urls import path


from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.photos import PhotoDetail

urlpatterns =[
    path("", IndexView.as_view(), name='index'),
    path("photo/", IndexRedirectView.as_view(), name='photos_index_redirect'),
    # path('photo/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/<int:pk>', PhotoDetail.as_view(), name='photo_detail'),
]


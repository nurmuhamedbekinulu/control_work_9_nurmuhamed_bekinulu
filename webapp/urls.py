from django.urls import path


from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.photos import PhotoDetail, PhotoCreateView, PhotoDeleteView, PhotoUpdateView, FavoriteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("photo/", IndexRedirectView.as_view(), name='photos_index_redirect'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/<int:pk>', PhotoDetail.as_view(), name='photo_detail'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/<int:pk>/confirm_delete/',
         PhotoDeleteView.as_view(), name='confirm_delete'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photos/<int:pk>/to-favorite',
         FavoriteView.as_view(), name='to_favorite'),
]

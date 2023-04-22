from django.urls import path

from api.views import PhotoView

urlpatterns = [
    path("photos/", PhotoView.as_view(), name='photos'),
]

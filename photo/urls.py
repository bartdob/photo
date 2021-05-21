from django.urls import path, include
from .views import PhotoListView, UserPhotoListView, PhotoCreateView, PhotoDetailView
from . import views


urlpatterns = [
    # path('', views.main, name='photo-page'),
    path('', PhotoListView.as_view(), name='photo-page'),
    path('user/<str:username>/', UserPhotoListView.as_view(), name='user-photos'),
    path('photo/new/', PhotoCreateView.as_view(), name='photo-create'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail')
]
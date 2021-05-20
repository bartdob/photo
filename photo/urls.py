from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.main, name='photo-page'),
    path('', PostListView.as_view(), name='photo-page'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-photo'),
    path('post/new/', PostCreateView.as_view(), name='photo-create'),
]
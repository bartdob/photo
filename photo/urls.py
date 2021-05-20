from django.urls import path, include
from . import views
from views import .

urlpatterns = [
    # path('', views.main, name='photo-page'),
    path('', PostListView.as_view(), name='photo-page'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-photo'),
    path('photo/new/', PostCreateView.as_view(), name='photo-create'),
]
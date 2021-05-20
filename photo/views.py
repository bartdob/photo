from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.core.paginator import Paginator
from django.contrib.auth.models import User
import requests
import os

def main(request):
    context = {
        'photos': Photo.objects.all()
    }
    return render (request, 'photo.html', context)

class PhotoListView(ListView):
    model = Photo
    template_name = 'index.html'
    context_object_name = 'photo'
    ordering = ['-date']
    paginate_by = 4

class UserPhotoListView(ListView):
    model = Photo
    template_name = 'user_photo.html'
    context_object_name = 'photo'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Photo.objects.filter(author=user).order_by('-date')


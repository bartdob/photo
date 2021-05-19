from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
import os

def main(request):
    return render (request, 'photo.html')

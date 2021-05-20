from django.shortcuts import render, redirect
import requests
import os

def main(request):
    return render (request, 'photo.html')

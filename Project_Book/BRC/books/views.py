
from .models import Book
from django.db import models
from django.contrib.auth.models import User


from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')



def store(request):

  return render(request, 'users/store.html')

def viewbook(request):
    return render(request, 'users/viewbook.html')






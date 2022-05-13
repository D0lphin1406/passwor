from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')
def password(request):
    thepassword = ''
    lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        lowercase_letters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('specsimbol'):
        lowercase_letters.extend('!#$%&*+-=?@^_')
    if request.GET.get('numbers'):
        lowercase_letters.extend('0123456789')
    for i in range(length):
        thepassword += random.choice(lowercase_letters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
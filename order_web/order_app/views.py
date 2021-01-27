from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session

# Create your views here.


def index_page(request):
    return render(request, 'index.html', {})

from urllib import response
from django.shortcuts import render
import requests
from .models import Quote

# Create your views here.

def index(request):
    quote = requests.get('https://api.kanye.rest/').json()
    context = {'quote':quote}
    return render (request, 'index.html', context)
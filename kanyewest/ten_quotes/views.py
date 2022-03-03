from urllib import response
from django.shortcuts import render
import requests
# from .models import Quote

# Create your views here.

def index(request):
    return render (request, 'index.html')

def get(request):
    quotes = []
    for x in range(2):
        quote = requests.get('https://api.kanye.rest/').json()
        quotes.append(quote)
    context = {'quote':quote, 'quotes':quotes}
    return render (request, 'index.html', context)
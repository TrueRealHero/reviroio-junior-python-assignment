from enum import unique
from operator import contains
from django.shortcuts import render, redirect
import requests
from .models import Quote

# Create your views here.

def index(request):
    return render (request, 'index.html')

def get(request):
    id_of_quotes = []
    for x in range(2):
        quote = Quote()
        json_quote = requests.get('https://api.kanye.rest/').json()
        sentence = list(json_quote.values())
        quote.kanye_quote = sentence
        if Quote.objects.filter(kanye_quote__contains = sentence):
            existing_quote = Quote.objects.get(kanye_quote__contains = sentence)
            id_of_quotes.append(existing_quote.id)
            continue
        letters_amount = int()
        for separate in sentence:
            words = separate.split()
        for word in words:
            word_len = len(word)
            letters_amount += word_len

        quote.letters_amount = letters_amount
        quote.save()
        id_of_quotes.append(quote.id)

    quotes = Quote.objects.filter(id__in = id_of_quotes)
    context = {'quotes':quotes}
    return render (request, 'index.html', context)
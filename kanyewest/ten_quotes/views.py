from django.shortcuts import render
import requests
from .models import Quote

# Create your views here.

def index(request):
    return render (request, 'index.html')

def get(request):
    id_of_quotes = []        # Для последующего записи ID, питон будет из этого списка фильтровать объекты
    for x in range(2):        # Получаем 10 цитат
        quote = Quote()
        json_quote = requests.get('https://api.kanye.rest/').json()       # Получаем цитату в джейсоне
        sentence = list(json_quote.values())                                # Вытаскиваем только квоту
        quote.kanye_quote = sentence                                         # Заполняем поле объекта
        if Quote.objects.filter(kanye_quote__contains = sentence):             # Чекаем на уникальность
            existing_quote = Quote.objects.get(kanye_quote__contains = sentence)
            id_of_quotes.append(existing_quote.id)
            continue

        # Логика подсчета букв без пробелов, гласных и согласных
        vowels_list = 'aeiouAEIOU'
        consonant_list = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        letters_amount = int()
        vowels = int()
        consonants = int()
        for words in sentence:                         
            for letter in words:
                if letter in vowels_list:
                    vowels += 1
                    letters_amount += 1
                elif letter in consonant_list :
                    consonants += 1
                    letters_amount += 1
        quote.vowels = vowels
        quote.consonants = consonants
        quote.letters_amount = letters_amount

        quote.save()
        id_of_quotes.append(quote.id)

    quotes = Quote.objects.filter(id__in = id_of_quotes)   # Вытаскием свежие цитаты, если она в ДБ, берет оттуда
    context = {'quotes':quotes}
    return render (request, 'index.html', context)
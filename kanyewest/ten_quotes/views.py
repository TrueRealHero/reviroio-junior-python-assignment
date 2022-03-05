from django.shortcuts import render
import requests
from .models import Quote
from collections import Counter

# Create your views here.

def index(request):
    return render (request, 'index.html')

def get_quote(request):
    id_of_quotes = []        # Для последующего записи ID, питон будет из этого списка фильтровать объекты
    for x in range(10):        # Получаем 10 цитат
        quote = Quote()         # Создаем объект
        json_quote = requests.get('https://api.kanye.rest/').json()       # Получаем цитату в джейсоне
        sentence = list(json_quote.values())        # Вытаскиваем только квоту

        clear_sentence = str(sentence)          # Убирает скобки чтобы сделать красивее
        characters_to_remove = "()[]"
        for character in characters_to_remove:
            clear_sentence = clear_sentence.replace(character, "")

        quote.kanye_quote = clear_sentence          # Заполняем поле в модели Quote

        if Quote.objects.filter(kanye_quote__contains = clear_sentence):             # Чекаем на уникальность
            existing_quote = Quote.objects.get(kanye_quote__contains = clear_sentence)
            id_of_quotes.append(existing_quote.id)
            continue

        # Логика подсчета букв без пробелов, а также гласных и согласных
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

        # Количество появлений каждой буквы, используя цитату без символов которая создана в начале
        each_letter_appearance = Counter(clear_sentence)
        quote.repeated_letters = each_letter_appearance

        # Средняя длинна слов
        splitted_sentence = clear_sentence.split()
        average_len = sum(len(word) for word in splitted_sentence) / len(splitted_sentence)
        quote.average_len = average_len

        # Длиннейшие три слова
        longest_words = sorted(splitted_sentence, key=len)
        quote.longest_words = longest_words[-3::]

        # Сохраняем объект
        quote.save()
        id_of_quotes.append(quote.id)

    quotes = Quote.objects.filter(id__in = id_of_quotes)   # Вытаскием свежие цитаты, если она в ДБ, берет оттуда
    context = {'quotes':quotes}
    return render (request, 'index.html', context)
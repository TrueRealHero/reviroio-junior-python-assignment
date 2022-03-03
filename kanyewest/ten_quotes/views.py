from urllib import response
from django.shortcuts import render
import requests
from collections import defaultdict
# from .models import Quote

# Create your views here.

def index(request):
    return render (request, 'index.html')

def get(request):
    quotes = []
    letters_in_sentence = []
    result = []
    i = 0
    j = 0
    for x in range(2):
        quote = requests.get('https://api.kanye.rest/').json()
        sentence = list(quote.values())
        quotes.append(sentence)
        letters_amount = int()
        for y in sentence:
            words = y.split()
        for word in words:
            z = len(word)
            letters_amount += z
        letters_in_sentence.append(letters_amount)
    while i < len(quotes) and j < len(letters_in_sentence):
        compilation = quotes[i], letters_in_sentence[j]
        result.append(compilation)
        i += 1
        j += 1

    context = {'sentence':sentence, 'letters_amount':letters_amount, 'letters_in_sentence':letters_in_sentence,
                'result':result}
    return render (request, 'index.html', context)


# a = requests.get('https://api.kanye.rest/').json()
# # my_dict = defaultdict(set)
# # for word in a.values.split():
# #         my_dict[len(word)].add(word)   
# print(a)
# y = list(a.values())
# for x in y:
#     print(x.split())
#     print(len(x))

# f = 'The world is our office'
# m = f.split()
# j = int()
# for x in m:
#     k = len(x)
#     j += k
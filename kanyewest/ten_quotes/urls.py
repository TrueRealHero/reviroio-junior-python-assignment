from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('kanye-sayings', views.get_quote, name='kanye-sayings')
]

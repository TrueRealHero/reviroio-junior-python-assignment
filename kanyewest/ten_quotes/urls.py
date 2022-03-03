from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('kanye-sayings', views.get, name='kanye-sayings')
]

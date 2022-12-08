from django.urls import path

from .views import (
        home, 
        numbers_to_words,
        numbers_to_speech
)


urlpatterns = [
    path('', home, name='homePage'),
    path('numbers_to_words/<int:number>/',numbers_to_words, name='numbers_to_words'),
    path('numbers_to_speech/<int:number>/', numbers_to_speech, name="numbers_to_speech")
]

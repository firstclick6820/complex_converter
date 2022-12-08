from django.urls import path, re_path

from .views import (
        home, 
        numbers_to_words,
        numbers_to_speech, 
        text_to_speech, 
        get_languages
)


urlpatterns = [
    path('', home, name='homePage'),
    path('numbers_to_words/<int:number>/',numbers_to_words, name='numbers_to_words'),
    path('numbers_to_words/<int:number>/<str:to_format>/',numbers_to_words, name='numbers_to_words'),
    path('numbers_to_speech/<int:number>/', numbers_to_speech, name="numbers_to_speech"),
    path('numbers_to_speech/<int:number>/<str:lang>/', numbers_to_speech, name="numbers_to_speech"),
    path('text_to_speech/<str:text>/', text_to_speech, name='text_to_speech'),  #If request with default language
    path('text_to_speech/<str:text>/<str:lang>/', text_to_speech, name='text_to_speech'), # if request with specific language
    path('get_languages/',get_languages, name="get_languages")
    
]
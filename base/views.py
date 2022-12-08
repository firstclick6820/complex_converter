
# Import modules from django
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# rest framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


# Import Json module
import json

# Import Num2words module for converting number into words
from num2words import num2words

# import gTTS module to convert text into speech
from gtts import gTTS



# Home Page Provide URL Tree and Basic Usage Information
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
    context = {
        "Home": "Welcome to Converter API Application",
         "URLs": {
             "Numbers To Words": '',
             "Text To Speech" : '',
             "Numbers To Speech" : '',
             "Speech To Text" : '',
         }
    }
    
    return JsonResponse(context, safe=False)






# Here We Convert taken number from the user and convert it to words or simply can say to text.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def numbers_to_words(request, number):
    
    if type(number) == int:
        target_number = int(number)
        
        result = num2words(target_number)

        context = {
            "Provided Number": number,
            "Converted to Words": result,
        }
        return JsonResponse(context, safe=False)
    
    
    
    return JsonResponse({"Error": "Invalid Param!", "Solution": "Provide Integer Number (22222) only."}, safe=False)
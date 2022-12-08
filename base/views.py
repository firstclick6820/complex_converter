
# Import modules from django
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse


from django.core.files import File
# rest framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions



from pathlib import Path
import os



# Import Json module
import json

# Import Num2words module for converting number into words
from num2words import num2words

# import gTTS module to convert text into speech
from gtts import gTTS, langs
from tempfile import TemporaryFile


# Home Page Provide URL Tree and Basic Usage Information
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
    context = {
        "Home": "Welcome to Converter API Application",
         "URLs": {
             "Numbers To Words": '/numbers_to_words/23235532323/', 
             "Get Languages": '/get_languages/',
             "Text To Speech" : '/text_to_speech/text/en/',
             "Numbers To Speech" : '/numbers_to_speech/2232323/en/',
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







# convert numbers to speech
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def numbers_to_speech(request, number, lang = ''):
    # now hard code the language but in future make it dynamic let the user to choose the language
    language = 'en'

    if lang and type(lang) == str:
        language = lang
    
    if type(number) == int:
        target_number = int(number)
        
        text_result = num2words(target_number)

        speech = gTTS(text=text_result, lang=language, slow=False)
        speech.save('default.mp3')
        new_path = './{}'.format('default.mp3')

        converted_audiofile = File(
            file=open(new_path, 'rb'),
                name=Path(new_path))
        
        
        converted_audiofile.name = Path(new_path).name
        converted_audiofile.size = os.path.getsize(new_path)
        return FileResponse(converted_audiofile, as_attachment=True)
    
    
    

    return JsonResponse({"Error": "Invalid Param!", "Solution": "Provide Integer Number (22222) only."}, safe=False)





# convert text to speech
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def text_to_speech(request, text, lang = ""):
    # now hard code the language but in future make it dynamic let the user to choose the language
    language = 'en'
    
    
    
    # Check if the user spicify the language or not
    if lang and type(lang) == str:
        language = lang
    if type(text) == str:
        target_text = str(text)
        


        speech = gTTS(text=target_text, lang=language, slow=False)
        speech.save('default.mp3')
        new_path = './{}'.format('default.mp3')

        converted_audiofile = File(
            file=open(new_path, 'rb'),
                name=Path(new_path))
        
        
        converted_audiofile.name = Path(new_path).name
        converted_audiofile.size = os.path.getsize(new_path)
        return FileResponse(converted_audiofile, as_attachment=True)
    
    
    

    return JsonResponse({"Error": "Invalid Param!", "Solution": "Provide Integer Number (22222) only."}, safe=False)






# Get Languages
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_languages(request):
    
    if request.method == "GET":
        return JsonResponse(langs._langs, safe=False)
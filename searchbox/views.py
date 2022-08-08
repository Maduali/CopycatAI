from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from searchbox.models import Search
from searchbox.serializers import searchboxSerializer
from ast import keyword
from multiprocessing import context
import nltk
import pycountry
import requests
import bs4
import time
import random  
import pandas as pd
import numpy as np
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from tabulate import tabulate
from facebook_scraper import *
import twint
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.corpus import wordnet 
from nltk.tokenize.treebank import TreebankWordDetokenizer
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from .models import Search
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
import keyword
import urllib.request
import threading
from urllib.error import HTTPError
from django.shortcuts import render

# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "AIzaSyDxmxqlopQ9hNrdd2u8tGwO3OMN46nyUSM"

# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "c7d1709b8ab514192"


set_user_agent(
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")

def check():
        try:
            requests.get('https://www.google.com/').status_code
            print('online')
        
        except:
            print('offline')
            time.sleep(10)
            check_again()
            
def check_again():
        try:
            requests.get('https://www.google.com/').status_code

        except:
            print('offline')
            time.sleep(5)
            check()




def index(request):

   global keywords
   global name_of_organization
   global type_of_organization

   keywords = request.session['keywords']
   name_of_organization = request.session['name_of_organization']
   type_of_organization = request.session['type_of_organization']      

   
   t = threading.Thread(target=looping)
   t.start()
   
   return redirect('plus/')

def looping():


   locations= ['international']
   places=list(pycountry.countries)

   for x in places:
      locations.append(x.name)

   subplaces =list(pycountry.subdivisions)


   locations=[x.lower() for x in locations]

   if type_of_organization == "GO":
      search=[]
      places_length= len(locations)
      z=0
      while z < places_length:
         search.append('government AGENCY on ' +keywords+  ':'+locations[z])
         z += 1
      x=0
      a=[]

      while x < places_length:

       check()
       print(x)
       query =  search[x]
       url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&num=1"
       data = requests.get(url).json()

       # get the result items
       search_items = data.get("items")
       # iterate over 10 results found
       for i, search_item in enumerate(search_items):

         # get the page title

         result = search_item.get("title")
         snippet = search_item.get("snippet")

         print(query + '\n\n')
         print(result + '\n')
         x += 1
 
class SearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset =Search.objects.all()
    serializer_class = searchboxSerializer
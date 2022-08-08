from __future__ import division
from ast import keyword
from json import JSONDecoder
import simplejson as json
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
from .forms import Registration_form1
from formtools.wizard.views import SessionWizardView
from .models import Registration
from .models import Locations
import urllib
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from django.http import HttpResponseRedirect

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






class ContactWizard(SessionWizardView):
    template_name = "home.html"

    def done(self, form_list, **kwargs):
       data = {k: v for form in form_list for k, v in form.cleaned_data.items()}
       instance = Registration.objects.create(**data)
       
        
       type_of_organization = data['type_of_organization']
       name_of_organization = data['name_of_organization']
       keywords = data['keywords']
       self.request.session['keywords'] = keywords 
       self.request.session['name_of_organization'] = name_of_organization
       self.request.session['type_of_organization'] = type_of_organization

       return redirect('searchbox/')
    
    


    def get(self, request, *args, **kwargs):

        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)


def reglocations(request):

    countries= ['international']
    sub_divisions =[]
    places=list(pycountry.countries)

    for x in places:
        countries.append(x.name)


    subplaces =list(pycountry.subdivisions)

    for y in subplaces:
        sub_divisions.append(y.name)

    countries=[x.lower() for x in countries] 
    sub_divisions=[y.lower() for y in sub_divisions]
    sub_divisions = sorted(sub_divisions)
    a_subdivisions = []
    b_subdivisions = []
    c_subdivisions = []
    d_subdivisions = []
    e_subdivisions = []
    f_subdivisions = []
    g_subdivisions = []
    h_subdivisions = []
    i_subdivisions = []
    j_subdivisions = []
    k_subdivisions = []
    l_subdivisions = []
    m_subdivisions = []
    n_subdivisions = []
    o_subdivisions = []
    p_subdivisions = []
    q_subdivisions = []
    r_subdivisions = []
    s_subdivisions = []
    t_subdivisions = []
    u_subdivisions = []
    v_subdivisions = []
    w_subdivisions = []
    x_subdivisions = []
    y_subdivisions = []
    z_subdivisions = []




    
    for z in sub_divisions:
        if z.startswith('a'):
          a_subdivisions.append(z)
        elif z.startswith('b'):
          b_subdivisions.append(z)
        elif z.startswith('c'):
          c_subdivisions.append(z)
        elif z.startswith('d'):
          d_subdivisions.append(z)
        elif z.startswith('e'):
          e_subdivisions.append(z)
        elif z.startswith('f'):
          f_subdivisions.append(z)
        elif z.startswith('g'):
          g_subdivisions.append(z)
        elif z.startswith('h'):
          h_subdivisions.append(z)
        elif z.startswith('i'):
          i_subdivisions.append(z)
        elif z.startswith('j'):
          j_subdivisions.append(z)
        elif z.startswith('k'):
          k_subdivisions.append(z)
        elif z.startswith('l'):
          l_subdivisions.append(z)
        elif z.startswith('m'):
          m_subdivisions.append(z)
        elif z.startswith('n'):
          n_subdivisions.append(z)
        elif z.startswith('o'):
          o_subdivisions.append(z)
        elif z.startswith('p'):
          p_subdivisions.append(z)
        elif z.startswith('q'):
          q_subdivisions.append(z)
        elif z.startswith('r'):
          r_subdivisions.append(z)
        elif z.startswith('s'):
          s_subdivisions.append(z)
        elif z.startswith('t'):
          t_subdivisions.append(z)
        elif z.startswith('u'):
          u_subdivisions.append(z)
        elif z.startswith('v'):
          v_subdivisions.append(z)
        elif z.startswith('w'):
          w_subdivisions.append(z)
        elif z.startswith('x'):
          x_subdivisions.append(z)
        elif z.startswith('y'):
          y_subdivisions.append(z)
        elif z.startswith('z'):
          z_subdivisions.append(z)
    return render(request, 'locations.html', {'json_list': countries, 'a_sub_list': a_subdivisions, 'b_sub_list':b_subdivisions, 'c_sub_list':c_subdivisions, 'd_sub_list':d_subdivisions, 'e_sub_list':e_subdivisions, 'f_sub_list':f_subdivisions, 'g_sub_list':g_subdivisions, 'h_sub_list':h_subdivisions, 'i_sub_list':i_subdivisions, 'j_sub_list':j_subdivisions, 'k_sub_list':k_subdivisions, 'l_sub_list':l_subdivisions, 'm_sub_list':m_subdivisions, 'n_sub_list':n_subdivisions, 'o_sub_list':o_subdivisions, 'p_sub_list':p_subdivisions, 'q_sub_list':q_subdivisions, 'r_sub_list':r_subdivisions, 's_sub_list':s_subdivisions, 't_sub_list':t_subdivisions, 'u_sub_list':u_subdivisions, 'v_sub_list':v_subdivisions, 'w_sub_list':w_subdivisions, 'x_sub_list':x_subdivisions, 'y_sub_list':y_subdivisions, 'z_sub_list':z_subdivisions,})



def reglocationspost(request):

  countries_checked = request.POST.getlist("countries")
  a_checked = request.POST.getlist("a_sub_list")
  b_checked = request.POST.getlist("b_sub_list")
  c_checked = request.POST.getlist("c_sub_list")
  d_checked = request.POST.getlist("d_sub_list")
  e_checked = request.POST.getlist("e_sub_list")
  f_checked = request.POST.getlist("f_sub_list")
  g_checked = request.POST.getlist("g_sub_list")
  h_checked = request.POST.getlist("h_sub_list")
  i_checked = request.POST.getlist("i_sub_list")
  j_checked = request.POST.getlist("j_sub_list")
  k_checked = request.POST.getlist("k_sub_list")
  l_checked = request.POST.getlist("l_sub_list")
  m_checked = request.POST.getlist("m_sub_list")
  n_checked = request.POST.getlist("n_sub_list")
  o_checked = request.POST.getlist("o_sub_list")
  p_checked = request.POST.getlist("p_sub_list")
  q_checked = request.POST.getlist("q_sub_list")
  r_checked = request.POST.getlist("r_sub_list")
  s_checked = request.POST.getlist("s_sub_list")
  t_checked = request.POST.getlist("t_sub_list")
  u_checked = request.POST.getlist("u_sub_list")
  v_checked = request.POST.getlist("v_sub_list")
  w_checked = request.POST.getlist("w_sub_list")
  x_checked = request.POST.getlist("x_sub_list")
  y_checked = request.POST.getlist("y_sub_list")
  z_checked = request.POST.getlist("z_sub_list")
  checked_items = countries_checked + a_checked + b_checked + c_checked + d_checked + e_checked + f_checked + g_checked + h_checked + i_checked + j_checked + k_checked + l_checked + m_checked + n_checked + o_checked + p_checked + q_checked + r_checked + s_checked + t_checked + u_checked + v_checked + w_checked + x_checked + y_checked + z_checked 
  
  delete_function = Locations.objects.all()
  delete_function.delete()
  
  for x in checked_items:
    print(x)
    my_locations= Locations(name=x)
    my_locations.save()

  return HttpResponse('TESTING', status=100) 
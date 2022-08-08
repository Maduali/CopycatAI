from rest_framework import routers
from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from searchbox import views

router = routers.DefaultRouter()
router.register(r'searchbox', views.SearchViewSet)

vue_urls = [
  path('', lambda request: HttpResponse(render(request, 'vue_index.html'))),
  path('another-path/', lambda request: HttpResponse(render(request, 'vue_index.html'))),
]


urlpatterns = [
    path('',views.index),
    path('api/', include(router.urls)),
    path('plus/', include(vue_urls)),
]
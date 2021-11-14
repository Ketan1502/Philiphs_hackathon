from django.contrib import admin
from django.urls import path
from philiphs import views

urlpatterns = [
   path('', views.index, name='index'),
   path('models', views.models, name='models'),
   path('result', views.result, name='result'),
   path('project', views.project, name='project'),
]

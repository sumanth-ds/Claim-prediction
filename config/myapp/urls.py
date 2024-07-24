# ProjectApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path("predict", views.predict, name='predict')
   ]

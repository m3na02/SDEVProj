from django.urls import path
from hotwireca.views import *
app_name = 'hotwireca'
urlpatterns = [
    path('home', home, name='home'),
    path('testlang', testlang, name='testlang'),
]


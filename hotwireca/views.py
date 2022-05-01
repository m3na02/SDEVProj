from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

def testlang(request):
    return HttpResponse(_('Welcome to language translation!'))

def home(request):
    return  render(request, "home.html")

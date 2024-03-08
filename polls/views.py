from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("DsWeb - 2024.1 - 20231014040004 - Lucas Henrique Barreto Demetrio")

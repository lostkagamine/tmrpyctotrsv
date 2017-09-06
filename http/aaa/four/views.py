from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('FOUR FOUR FOUR FOUR, THE NUMBER 4')
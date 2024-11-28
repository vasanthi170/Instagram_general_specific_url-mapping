from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def messages(request):
    return HttpResponse ('You can interact with your friends heree...')
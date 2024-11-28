from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def find(request):
    return HttpResponse('you can search the content here!!!')
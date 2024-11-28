from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def content(request):
    return HttpResponse('<h1>Instagram feed:</h1>The content which was shared by your followers are displayed here!')
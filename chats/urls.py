from django.urls import path
from chats.views import*

urlpatterns=[
    path('messages/',messages,name='messages')
]
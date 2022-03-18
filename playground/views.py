from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, World!")  #  request 요청하다( Client - 클라이언트 )Chrome  /  response 응답하다( Server - 서빙 )Django


from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.

def login_user(request):
    return (request,'authenticate/login.html',{})
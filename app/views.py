#- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am a bold font from the context"}
    return render_to_response('HTML/index.html', context_dict, context) #need to redirect to new page

@csrf_exempt
def inbox(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am a bold font from the context"}
    return render_to_response('HTML/inbox.html', context_dict, context) #need to redirect to new page

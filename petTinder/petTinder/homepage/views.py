# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from editprofile.models import UserProfile

# Create your views here.

@login_required
def homepage(request):
    try:
        myAccount=UserProfile.objects.filter(userid=request.user.id)[0]
    except IndexError:
        myAccount=None
    context=dict(myAccount=myAccount, user=request.user)
    return render(request,'homepage.html',context)

@login_required
def logoutuser(request):
    logout(request)
    return redirect('/login/')

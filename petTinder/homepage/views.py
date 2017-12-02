# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def homepage(request):
    try:
        petTinder=(User.objects
           .exclude(id=request.user.id)
           .order_by('?')[0])
    except IndexError:
        petTinder=None
    context=dict(petTinder=petTinder)
    return render(request,'homepage.html',context)

def logoutuser(request):
##    auth_log(request)
#    context=None
##    return render(request,'register',context)
#    return redirect('register')
    logout(request);
    return redirect('/login/')


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import models

#from .models import Pets
# Create your views here.

@login_required
def allUsers(request):
    try:
        userList = []
        userList = User.objects.all()
    except IndexError:
        userList=None
    context=dict(userList=userList)
    return render(request,'userlist.html',context)


#@login_required
#def following(request, id):

#    return render(request,'following.html',context)

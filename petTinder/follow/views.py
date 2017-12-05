# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import models

from petlist.models import Pets
# Create your views here.

@login_required
def allusers(request):
    try:
        userList = []
        userList = (User.objects
                    .exclude(username=request.user))
    except IndexError:
        userList=None
    context=dict(userList=userList)
    return render(request,'userlist.html',context)

@login_required
def otherPetList(request, username=None):
    try:
        userPetList=[]
        userPetList=(Pets.objects
                     .filter(user__username=username))
        #numPets = len(userPetList)
    except IndexError:
        userPetList=None
        #numPets = '0'
    context=dict(userPetList=userPetList)
    #context=dict(userPetList=userPetList, numPets=numPets)
    return render(request,'otherpetlist.html',context)

@login_required
def followingList(request, id):

    return render(request,'following.html',context)

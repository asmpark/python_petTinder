# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import models

from petlist.models import Pets
from follow.models import FollowStruct
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
        userPetList = []
        userPetList = (Pets.objects
                     .filter(user__username=username))
    except IndexError:
        userPetList=None
    context=dict(userPetList=userPetList)
    return render(request,'otherpetlist.html',context)

def createFollow(request, followUser, followYN):
    models.FollowStruct.objects.create(
        userFrom = request.user,
        userTo = followUser,
        follow = followYN,
    )
    return redirect('allusers')

@login_required
def clickFollow(request,username=None):
    return createFollow(request, username, True)

@login_required
def followingList(request):
    try:
        followList = []
        followList = (FollowStruct.objects
                  .filter(userFrom = request.user)
                  .filter(follow = 'True'))
    except IndexError:
        followList=None
    context=dict(followList=followList)
    return render(request,'following.html',context)

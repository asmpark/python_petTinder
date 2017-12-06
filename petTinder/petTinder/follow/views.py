# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from petlist.models import Pets
from . import models
from follow.models import FollowStruct
# Create your views here.

@login_required
def allusers(request):
    try:
        userList = (User.objects.exclude(username=request.user.username))
        userListFollowing = []
        for user in userList:
            try:
                follow=FollowStruct.objects.filter(user=request.user.id).filter(follow_id=user.id)[0]
            except IndexError:
                models.FollowStruct.objects.create(
                    user=request.user.id,
                    follow_user=user.username,
                    follow_id=user.id,
                    following='False')
                follow=FollowStruct.objects.filter(user=request.user.id).filter(follow_id=user.id)[0]
            userListFollowing.append(follow)
    except IndexError:
        userList=None
        userListFollowing=None
    context=dict(userList=userList, userListFollowing=userListFollowing)
    return render(request,'userlist.html',context)

@login_required
def otherPetList(request, user_id):
    try:
        otherUser=User.objects.filter(id=user_id)[0]
        userPetList = (Pets.objects
                     .filter(user=otherUser))
    except IndexError:
        userPetList=None
    context=dict(userPetList=userPetList)
    return render(request,'otherpetlist.html',context)

@login_required
def clickFollow(request,follow_id):
    try:
        follow=FollowStruct.objects.filter(user=request.user.id).filter(follow_id=follow_id)[0]
        follow.following='True'
        follow.save()
    except IndexError:
        models.FollowStruct.objects.create(
            user=request.user.id,
            follow_user=follow_user.username,
            follow_id=follow_id,
            following='True')
    return redirect('allusers')

@login_required
def followingList(request):
    try:
        followList = (FollowStruct.objects
                        .filter(user = request.user.id)
                        .filter(following='True'))
    except IndexError:
        followList=None
    context=dict(followList=followList)
    return render(request,'following.html',context)

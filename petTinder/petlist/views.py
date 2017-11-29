# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User,Pets
from django.contrib.auth.decorators import login_required

from . import models, forms

# Create your views here.

@login_required
def userpets(request):
    try:
        userPetList=(Pets.objects
                     .where(id=request.user.id))
#        userPetList=(User.objects
#                   .exclude(id=request.user.id)
#                   .order_by('?')[0])
    except IndexError:
        userPetList=None
    context=dict(userPetList=userPetList)
    return render(request,'petlist.html',context)

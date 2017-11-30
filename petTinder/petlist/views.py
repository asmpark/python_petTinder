# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import models, forms

from petlist.models import Pets
from .forms import PetForm

# Create your views here.

@login_required
def userpets(request):
    try:
        userPetList=(Pets.objects
                     .filter(id=request.user.id))
    except IndexError:
        userPetList=None
    context=dict(userPetList=userPetList)
    return render(request,'petlist.html',context)

@login_required
def create_pet(request):
#def create_pet(request, user_id):
#    user=User.objects.get(pk=user_id)
#    newpet = Pets(
#        user=request.user,
#        pet_name=request.pet_name,
#        pet_photo=request.pet_photo,
#        pet_bio=request.pet_bio,
#    )
#    newpet.save()
    return render(request,'createpet.html')

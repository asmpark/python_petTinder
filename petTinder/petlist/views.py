# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import models, forms

from .models import Pets
from .forms import PetForm

# Create your views here.

@login_required
def userpets(request):
    try:
        userPetList=[]
        userPetList=(Pets.objects
                     .filter(user=request.user))
    except IndexError:
        userPetList=None
    context=dict(userPetList=userPetList)
    return render(request,'petlist.html',context)

@login_required
def create_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            newpet = form.save(commit=False)
            newpet.user = request.user
            newpet.pet_name=request.POST['pet_name']
            newpet.pet_photo=request.FILES['pet_photo']
            newpet.pet_bio=request.POST['pet_bio']
            newpet.save()
            return redirect('userpets')
    else:
        form = PetForm()
    return render(request, 'createpet.html', {'form': form})



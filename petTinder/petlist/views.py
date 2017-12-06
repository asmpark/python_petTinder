# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

from . import models, forms

from .models import Pets
from .forms import PetForm
from swipe.models import PetVote

# Create your views here.

@login_required
def userpets(request):
    try:
        userPetList=[]
        userPetList=(Pets.objects
                     .filter(user=request.user))
        numPets = len(userPetList)
    except IndexError:
        userPetList=None
        numPets = '0'
    context=dict(userPetList=userPetList, numPets=numPets)
    return render(request,'petlist.html',context)

@login_required
def create_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            newpet = form.save(commit=False)
            newpet.user = request.user
            newpet.pet_name=request.POST['pet_name']
            # newpet.pet_photo=request.FILES['pet_photo']
            # newpet.pet_photo2=request.FILES['pet_photo2']
            # newpet.pet_photo3=request.FILES['pet_photo3']
            # newpet.pet_photo4=request.FILES['pet_photo4']
            # newpet.pet_photo5=request.FILES['pet_photo5']
            # newpet.pet_photo6=request.FILES['pet_photo6']
            #
            # try:
            #     newpet.pet_photo=request.FILES['pet_photo']
            # except MultiValueDictKeyError:
            #     newpet.pet_photo=None
            try:
                newpet.pet_photo2=request.FILES['pet_photo2']
            except MultiValueDictKeyError:
                newpet.pet_photo2=None
            try:
                newpet.pet_photo3=request.FILES['pet_photo3']
            except MultiValueDictKeyError:
                newpet.pet_photo3=None
            try:
                newpet.pet_photo4=request.FILES['pet_photo4']
            except MultiValueDictKeyError:
                newpet.pet_photo4=None
            try:
                newpet.pet_photo5=request.FILES['pet_photo5']
            except MultiValueDictKeyError:
                newpet.pet_photo5=None
            try:
                newpet.pet_photo6=request.FILES['pet_photo6']
            except MultiValueDictKeyError:
                newpet.pet_photo6=None
            newpet.pet_bio=request.POST['pet_bio']
            newpet.save()
            return redirect('userpets')
    else:
        form = PetForm()
    return render(request, 'createpet.html', {'form': form})

@login_required
def del_pet(request, pet_id):
    Pets.objects.filter(id=pet_id).delete()
    PetVote.objects.filter(pet_id=pet_id).delete()
    return redirect('userpets')

@login_required
def edit_pet(request, pet_id):
    try:
        editpet = Pets.objects.filter(id=pet_id)[0]
        form = PetForm(initial={
            'pet_name': editpet.pet_name,
            'pet_photo': editpet.pet_photo,
            'pet_photo2': editpet.pet_photo2,
            'pet_photo3': editpet.pet_photo3,
            'pet_photo4': editpet.pet_photo4,
            'pet_photo5': editpet.pet_photo5,
            'pet_photo6': editpet.pet_photo6,
            'pet_bio': editpet.pet_bio})
    except IndexError:
        editpet=None
        form=PetForm()
    context=dict(form=form, pet=editpet)
    return render(request,'editpet.html',context)

@login_required
def edit_this_pet(request, pet_id):
    if request.method=='POST':
        try:
            editpet=Pets.objects.filter(id=pet_id)[0]
            form=PetForm(request.POST,request.FILES,instance=editpet)
            if form.is_valid():
                edits=form.save(commit=False)
                edits.user=request.user
                edits.pet_name=request.POST['pet_name']
                try:
                    edits.pet_photo=request.FILES['pet_photo']
                except MultiValueDictKeyError:
                    edits.pet_photo=editpet.pet_photo
                try:
                    edits.pet_photo2=request.FILES['pet_photo2']
                except MultiValueDictKeyError:
                    edits.pet_photo2=editpet.pet_photo2
                try:
                    edits.pet_photo3=request.FILES['pet_photo3']
                except MultiValueDictKeyError:
                    edits.pet_photo3=editpet.pet_photo3
                try:
                    edits.pet_photo4=request.FILES['pet_photo4']
                except MultiValueDictKeyError:
                    edits.pet_photo4=editpet.pet_photo4
                try:
                    edits.pet_photo5=request.FILES['pet_photo5']
                except MultiValueDictKeyError:
                    edits.pet_photo5=editpet.pet_photo5
                try:
                    edits.pet_photo6=request.FILES['pet_photo6']
                except MultiValueDictKeyError:
                    edits.pet_photo6=editpet.pet_photo6
                edits.pet_bio=request.POST['pet_bio']
                edits.save()
                return redirect('userpets')
        except IndexError:
            form=PetForm()
    else:
        form=PetForm()
    return redirect('userpets')

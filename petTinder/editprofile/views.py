# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import models, forms

from petlist.models import Pets
from swipe.models import PetVote

# Create your views here.

@login_required
def profile(request):
    try:
        curr_user = request.user
        profile=request.user
#        profile=request.user.userprofile
        petTinder=User.objects
    except models.UserProfile.DoesNotExist:
        profile=None
        curr_user=None
    if request.method=='POST':
        form=forms.UserProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            if profile:
                form.save()
            else:
                profile=form.save(commit=False)
                profile.user=request.user
                profile.save()
    form=forms.UserProfileForm(instance=profile)
    context=dict(form=form, curr_user=curr_user)
    return render(request,'profile.html',context)

@login_required
def del_user(request):
    try:
#        from .models import Pets, PetVote
        u = User.objects.get(username = request.user)
        Pets.objects.filter(user_id=request.user.id).delete()
        PetVote.objects.filter(user_id=request.user.id).delete()
        u.delete()
        return redirect('/login/')
    
    except User.DoesNotExist:
        messages.error(request, "User does not exist")
        return render(request,'homepage.html')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from . import models, forms

from petlist.models import Pets
from swipe.models import PetVote
from editprofile.models import UserProfile
from .forms import UserProfileForm

# Create your views here.

@login_required
def profile(request):
    try:
        curr_user = request.user
        profile=request.user.userprofile
    except models.UserProfile.DoesNotExist:
        profile=None
        curr_user=None

    ##DOESN'T WORK PROPERLY
    if request.method=='POST':
        instance = request.user.userprofile
        form = UserProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
#            form=form.save(commit=False)
            form.user=instance
            form.photo=request.FILES['photo']
            form.bio=request.POST['bio']
            form.save()
    else:
        form = UserProfileForm()
    context=dict(form=form, curr_user=curr_user)
    return render(request,'profile.html',context)

@login_required
def del_user(request):
    try:
        u = User.objects.get(username = request.user)
        Pets.objects.filter(user_id=request.user.id).delete()
        PetVote.objects.filter(user_id=request.user.id).delete()
        u.delete()
        return redirect('/login/')
    
    except User.DoesNotExist:
        messages.error(request, "User does not exist")
        return render(request,'homepage.html')

@login_required
def changePW(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/login/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changePW.html', {'form': form})

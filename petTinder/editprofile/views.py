# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import FieldDoesNotExist, MultipleObjectsReturned
from django.utils.datastructures import MultiValueDictKeyError

from . import models, forms

from petlist.models import Pets
from swipe.models import PetVote
from editprofile.models import UserProfile
from .forms import UserProfileForm

# Create your views here.

@login_required
def profile(request):
    try:
        profile=UserProfile.objects.filter(userid=request.user.id)[0]
        form = UserProfileForm(initial={'photo': profile.photo, 'bio': profile.bio})
    except IndexError:
        profile=None
        form=UserProfileForm()
    context=dict(form=form)
    return render(request,'profile.html',context)

@login_required
def edit_profile(request):
    if request.method=='POST':
        try:
            profile=UserProfile.objects.filter(userid=request.user.id)[0]
        except IndexError:
            form=UserProfileForm(request.POST,request.FILES)
            if form.is_valid():
                newprof=form.save(commit=False)
                newprof.user=request.user
                newprof.userid=request.user.id
                newprof.photo=request.FILES.get('photo')
                newprof.bio=request.POST['bio']
                newprof.save()
                return redirect('homepage')
        form=UserProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            oldprof=form.save(commit=False)
            oldprof.user=request.user
            oldprof.userid=request.user.id
            try:
                oldprof.photo=request.FILES['photo']
            except MultiValueDictKeyError:
                oldprof.photo=profile.photo
            oldprof.bio=request.POST['bio']
            oldprof.save()
    else:
        form=UserProfileForm()
    return redirect('homepage')

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

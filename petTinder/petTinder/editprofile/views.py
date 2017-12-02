# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import models, forms

# Create your views here.

@login_required
def profile(request):
    try:
        profile=request.user.userprofile
        petTinder=User.objects
    except models.UserProfile.DoesNotExist:
        profile=None
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
    context=dict(form=form)
    return render(request,'profile.html',context)

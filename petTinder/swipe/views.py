# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from petlist.models import Pets

from . import models, forms

# Create your views here.

@login_required
def index(request):
    try:
        petTinder=(Pets.objects
                   .exclude(user=request.user)
                   .order_by('?')[0])
    except IndexError:
        petTinder=None
    context=dict(petTinder=petTinder)
    return render(request,'index.html',context)

def create_vote(request,user_id, vote):
    user=User.objects.get(pk=user_id)
    models.UserVote.objects.create(
       user=user,
       voter=request.user,
       vote=vote,
    )
    return redirect('index')

@login_required
def like(request,user_id):
    return create_vote(request, user_id, True)

@login_required
def nah(request, user_id):
    return create_vote(request,user_id, False)


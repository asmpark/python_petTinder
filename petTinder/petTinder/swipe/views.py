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

def create_vote(request,pet_id, vote):
    ##FIXFIXFIX
    user_id=User.objects.only('id').get(id=request.user.id)
    pet_id=Pets.objects.only('id').get(id=pet_id)
    models.UserVote.objects.create(
       user_id=user_id,
       pet_id=pet_id,
       vote=vote,
    )
    return redirect('index')

@login_required
def like(request,pet_id):
    return create_vote(request, pet_id, True)

@login_required
def nah(request, pet_id):
    return create_vote(request,pet_id, False)


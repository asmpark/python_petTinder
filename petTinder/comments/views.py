# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

from . import models, forms

from petlist.models import Pets
from comments.models import Comments
from comments.forms import CommentForm

# Create your views here.

@login_required
def comment(request,pet_id):
    if request.method=='POST':
        form=CommentForm(request.POST)
        try:
            check_owns = Pets.objects.filter(user=request.user).filter(id=pet_id)[0]
            owns='True'
        except IndexError:
            owns='False'
        if form.is_valid():
            newcom = form.save(commit=False)
            newcom.user_id=request.user.id
            newcom.pet_id=pet_id
            newcom.owns=owns
            newcom.post=request.POST['post']
            newcom.save()
    else:
        form=CommentForm()
    try:
        commentList=(Comments.objects.filter(pet_id=pet_id))
    except IndexError:
        commentList=None
    context=dict(form=form, commentList=commentList, pet_id=pet_id)
    return render(request,'comments.html',context)

@login_required
def del_com(request,com_id):
    Comments.objects.filter(id=com_id).delete()
    return redirect('userpets')

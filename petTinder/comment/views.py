# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import models, forms

from .forms import CommentForm
from comment.models import CommentStruct
from petlist.models import Pets
from follow.views import allusers

# Create your views here.
@login_required
def writeComment(request,petid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            newcomment = form.save(commit=False)
            newcomment.user = request.user
            newcomment.pet_id = petid
            newcomment.commentwords=request.POST[commentwords]
            newcomment.save()
            #return redirect('showComment', petid) #temp
    else:
        form = CommentForm()
    return render(request,'writingComment.html',{'form':form})

def showComment(request, petid):
    try:
        commentList=[]
        commentList = (CommentStruct.objects
                      .filter(pet_id=petid)
                      .filter(user=request.user))
    except IndexError:
        commentList=None
    context=dict(commentList=commentList)
    return render(request,'commentlist.html',context)

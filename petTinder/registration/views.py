# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=UserCreationForm()
    context=dict(form=form)
    return render(request,'registration/newuser.html',context)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth import User
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    photo=models.ImageField(upload_to='photos')
    bio=models.TextField()
    
    def __unicode__(self):
        return self.user.get_username()

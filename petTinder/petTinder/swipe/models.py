# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from editprofile.models import UserProfile
from petlist.models import Pets

# Create your models here.

class UserVote(models.Model):
#    user=models.ForeignKey(User)
    user_id=models.ForeignKey(User, id)
    pet_id=models.ForeignKey(Pets, id)
    vote=models.BooleanField(default=False)
                            
    class Meta:
         unique_together=(('user_id','pet_id'))

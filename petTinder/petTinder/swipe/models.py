# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from petlist.models import Pets

# Create your models here.

class PetVote(models.Model):
    user_id=models.IntegerField(default='0')
    pet_id=models.IntegerField(default='0')
    vote=models.BooleanField(default=False)
                            
    class Meta:
         unique_together=(('user_id','pet_id'))


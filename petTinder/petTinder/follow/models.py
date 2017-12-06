# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FollowStruct(models.Model):
    user=models.IntegerField(default='0')
    follow_id=models.IntegerField(default='0')
    follow_user=models.CharField(max_length=50, default="")
    following=models.BooleanField(default='False')

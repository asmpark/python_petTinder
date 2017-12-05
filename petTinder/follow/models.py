# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FollowStruct(models.Model):
    userFrom = models.ForeignKey(User, related_name = 'userFrom') #followee
    userTo = models.ManyToManyField("self", related_name = 'userTo') #following
    #userFrom_id = models.IntegerField(default='0')
    #userTo_id = models.IntegerField(default='0')
    follow = models.BooleanField(default=False)

    #class Meta:
    #    unique_together=(('userFrom','userTo'))

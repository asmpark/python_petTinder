# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comments(models.Model):
    user_id=models.IntegerField()
    pet_id=models.IntegerField()
    post=models.TextField()
    owns=models.BooleanField(default='False')

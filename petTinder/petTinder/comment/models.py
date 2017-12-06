# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from petlist.models import Pets

# Create your models here.

class CommentStruct(models.Model):
    user=models.IntegerField(default=0)
    pet_id=models.OneToOneField(Pets, default=None)
    comment_id=models.IntegerField(default=0)
    commentwords=models.TextField()

    def __unicode__(self):
        return self.user.get_username()

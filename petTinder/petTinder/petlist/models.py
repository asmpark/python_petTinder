# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from editprofile.models import UserProfile

# Create your models here.

class Pets(models.Model):
    user=models.ForeignKey(User)
    pet_name=models.CharField(max_length=30)
    pet_photo=models.ImageField(upload_to='photos')
    pet_photo2=models.ImageField(upload_to='photos', blank=True, null=True)
    pet_photo3=models.ImageField(upload_to='photos', blank=True, null=True)
    pet_photo4=models.ImageField(upload_to='photos', blank=True, null=True)
    pet_photo5=models.ImageField(upload_to='photos', blank=True, null=True)
    pet_photo6=models.ImageField(upload_to='photos', blank=True, null=True)
    pet_bio=models.TextField()

    def __unicode__(self):
        return self.user.get_username()

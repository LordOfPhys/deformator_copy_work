# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name='user', related_name='my_profile')
    site_adress = models.CharField(max_length = 30, default='web_site')
    def __unicode__(self):
        return self.user.username
    def __get_url__(self):
        return self.site_adress
    def __add_url__(self, site):
        self.site_adress = site
        self.save()

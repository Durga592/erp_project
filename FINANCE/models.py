# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Module_Names(models.Model):
	module_name			=	models.CharField("MODULE NAME", max_length=250)
	resource_name		=	models.CharField("RESOURCE NAME", max_length=250)
	module_duration		=	models.CharField("MODULE DURATION", max_length=250)
	client_name			=	models.CharField("CLIENT NAME", max_length=250)
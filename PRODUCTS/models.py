# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Details(models.Model):
	product_name		=	models.CharField("PRODUCT NAME", max_length=250)
	technologies		=	models.CharField("TECHNOLOGIES", max_length=250)
	client				=	models.CharField("CLIENT", max_length=250)
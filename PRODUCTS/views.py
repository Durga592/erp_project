# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Details
# Create your views here.
def creation(request):
	#return HttpResponse("hello")
	print request.method
	print request.POST
	msg 				=	''
	if request.method 	== 'POST':
		print request.POST['productname']
		prod_instance	=	Details(product_name	=	request.POST['productname'],
									technologies	=	request.POST['techname'],
									client			=	request.POST['client'])
		prod_instance.save()
		msg				=	'Successfully Product Created'
	all_data			=	Details.objects.all()
	return render(request, "products/products.html", {"data":all_data, "suc_msg":msg})

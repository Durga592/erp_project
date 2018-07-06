# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Module_Names
# Create your views here.
def finance_modules(request):
	#return HttpResponse("hello")
	print request.method
	print request.POST
	msg 				=	''
	if request.method 	== 'POST':
		print request.POST['modulename']
		fin_instance	=	Module_Names(module_name		=	request.POST['modulename'],
									resource_name	=	request.POST['resourcename'],
									module_duration	=	request.POST['duration'],
									client_name		=	request.POST['clientname'])
		fin_instance.save()
		msg				=	'Successfully Finance Module Created'
	module_data			=	Module_Names.objects.all()
	return render(request, "erp/finance_modules.html", {"fin_data":module_data, "suc_msg":msg})

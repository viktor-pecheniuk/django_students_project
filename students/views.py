# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# from django.template import RequestContext, loader

def students_list(request):
	students = (
		{'id' : 1,
		'first_name': u'Віктор',
		'last_name': u'Печенюк',
		'ticket': 254,
		'image': u'img/foto'},
		{'id' : 2,
		'first_name': u'Олесь',
		'last_name': u'Попов',
		'ticket': 2123,
		'image': u'img/foto',
		},
		{'id' : 3,
		'first_name': u'Василь',
		'last_name': u'Гуменюк',
		'ticket': 25431,
		'image': u'img/foto',
		},
	)
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

def groups_list(request):
	return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
	return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
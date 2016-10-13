from django.shortcuts import render
from django.http import HttpResponse

from todo.models import list_item

def index(request, ):
	todo_list = list_item.objects.all()
	print todo_list
	return HttpResponse("Hie there!")

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Person

# Create your views here.

def index(request):
	response = HttpResponse()
	response.write('<img src="media/banner32.jpg" alt="My friends site banner" width=100% height=320/>')
	response.write('<body style=background-image:url("media/bg2.jpg")>')
	return response

def details(request,pid=0):
	p=get_object_or_404(Person,pk=pid)
	return render(request, 'person_details.html', {'p':p})

from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.

def index(request):
	response = HttpResponse()
	response.write('<html><body>')
	response.write('<h1>Python Friends Site<h1>')
	plist = Person.objects.all()
	for p in plist:
		link = '<a href="friends/info/%d">'%p.id
		response.write('<li>%s%s</a></li>'%(link,p.name))
	response.write('</body></html>')
	return response

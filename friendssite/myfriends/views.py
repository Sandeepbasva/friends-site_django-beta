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

def details(request,pid=0):
	response = HttpResponse()
	response.write('<html><body>')
	try:
		p=Person.objects.get(id=pid)
		response.write('<h1>Details of Person %s</h1><hr>'%p.name)
		response.write('<li>Gender: %s</li>'%p.gender)
		response.write('<li>Birthday: %s</li>'%p.birthday)
		response.write('<li>Favourite URL: %s</li>'%p.favouriteURL)
		response.write('<li>Message: %s</li>'%p.description)
	
	except Person.DoesNotExist:
		print('The person details does not exist')
	
	response.write('</body></html>')
	return response

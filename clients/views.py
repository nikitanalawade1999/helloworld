from django.shortcuts import render
from django.http import HttpResponse
from .models import Drivers
# Create your views here.
	#return HttpResponse('<h1>Hello, I am learning Django!</h1>')
def clientsListing(request):
	clientlistings=Drivers.objects.all()
	print("Received driver Records",len(clientlistings))
	context={
	    'driverList': clientlistings,
	    'name':'Nikita'
	}

	return render(request,'clients/clients.html',context)# Create your views here.

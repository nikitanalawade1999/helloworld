from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def homemenu(request):
	#return HttpResponse('<h1>Hello, I am learning Django!</h1>')
	return render(request,'menu/home.html')
def contactmenu(request):
	return render(request,'menu/contact.html')
def login1menu(request):
	if request.method == 'POST':
		print("I am in POST request")
		unameEntered=request.POST['usernamesignup']
		passEntered=request.POST['passwordsignup']
		print("username :",unameEntered)
		userObject = auth.authenticate(username=unameEntered, password=passEntered)
		if userObject is not None:
			auth.login(request,userObject)
			print("User logged in")
			return redirect('myhome')
		else:
			messages.error(request,"Username/password invalid")
			return redirect("mylogin1")
	else:
		return render(request,'menu/login1.html')

	

def registermenu(request):
	if request.method == 'POST':
		username=request.POST['usernamesignup']
		email=request.POST['emailsignup']
		password1=request.POST['passwordsignup']
		password2=request.POST['passwordsignup_confirm']
		print("username:",username)
		print("email:",email)
		print("password1:",password1)
		print("password2:",password2)

		if(password1== password2):
			if User.objects.filter(username=username).exists():
				print('The username available/its already exists')
				return redirect('myregister')
			else:
				user=User.objects.create_user(username=username,password=password1,email=email)
				user.save()
				print('You are now registered and can login')
				return redirect('mylogin1')
		else:
			messages.error(request,'password do not match,please enter again')
			return redirect('myregister')
		           
		
	else:
		print("I am in GET request")
		return render(request,'menu/register.html')
def logoutmenu(request):
	print("In logout")
	auth.logout(request)
	return redirect('mylogin1')

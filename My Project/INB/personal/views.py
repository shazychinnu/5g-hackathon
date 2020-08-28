from django.shortcuts import render
from .forms import applicationform
from .models import customer_information
import random
from datetime import date,datetime
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

#Account application Form

def home(request):
	context ={}
	# return HttpResponse ('<h1>Hello</h1>')
	return render(request,'home.html',context)

def application(request):
	#GET METHOD
	form = applicationform()
	context = {'form':form}
	#POST METHOD
	if request.method == 'POST':
		form=applicationform(request.POST)
		if form.is_valid():
			registration_time = date.today()
			registration_number = random.randint(33333111101,99999999999)
			Name = request.POST['Name']
			email = request.POST['email']
			gender = request.POST['gender']
			address = request.POST['address']
			MobileNum = request.POST['MobileNum']
			Password = request.POST['Password']
			city = request.POST['city']
			profession = request.POST['profession']
			app_obj = customer_information(registration_time=registration_time,registration_number=registration_number,Name=Name,
				email=email,gender=gender,address=address,MobileNum=MobileNum,Password=Password,city=city,profession=profession)
			app_obj.save()
			return render(request,'thanks.html',{'app_req_num':registration_number,'name':Name})
		else:
			return HttpResponse("NOT VALID")
	return render(request,'Account_opening.html',{'form':form})


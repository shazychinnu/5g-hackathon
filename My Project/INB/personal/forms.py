from django import forms
from crispy_forms.helper import FormHelper
from .models import customer_information
import random


class applicationform(forms.Form):
	# acc_opening_time = forms.DateField(label='Date:YYYY-MM-DD',)
	Name = forms.CharField(required=True,widget = forms.TextInput(
		attrs={'placeholder':'Enter Surname'}))
	email = forms.EmailField(label='E-Mail',required=True,widget = forms.TextInput(
		attrs={'placeholder':'Enter Emil Id'}))
	options =(('select','select'),('Male',"Male"),('Female',"Female"))
	gender = forms.ChoiceField(choices = options)
	address = forms.CharField(widget = forms.Textarea(
		attrs={'placeholder':'Enter Complete Address'}))
	MobileNum = forms.IntegerField(label='Mob_num',required=True,widget = forms.TextInput(
		attrs={'placeholder':'Enter mobile Number'}))
	Password = forms.CharField(label = 'Enter Password',widget=forms.PasswordInput(
		attrs={'placeholder':'Enter password'}))
	options =(('select','select'),('Mumbai',"Mumbai"),('Delhi',"Delhi"),('Bangalore',"Bangalore"),('Hyderabad',"Hyderabad"),
		('Ahmedabad',"Ahmedabad"),('Chennai',"Chennai"),('Kolkata',"Kolkata"),('Lucknow',"Lucknow"),
		('Indore',"Indore"),('Bhopal',"Bhopal"),('Visakhapatnam',"Visakhapatnam"),('Varanasi',"Varanasi"))
	city = forms.ChoiceField(choices = options)
	options =(('select','select'),('student',"student"),('Startup SME',"Startup SME"),('Corporate professional',"Corporate professional"))
	profession = forms.ChoiceField(choices = options)
class customer_informationForm(forms.ModelForm):
	class Meta:
		model = customer_information
		fields = ('registration_time','registration_number','Name','email','gender','address','MobileNum','Password','city','profession')
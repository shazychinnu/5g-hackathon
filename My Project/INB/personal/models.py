from django.db import models
from datetime import datetime,date

# Create your models here.
class customer_information(models.Model): 
	# CourseId=models.AutoField(primary_key=True,default=00)
	registration_time = models.DateField(default='YYYY-MM-DD')
	registration_number = models.IntegerField(default=True,unique=True)
	Name = models.CharField(max_length=50)
	email = models.EmailField()
	gender = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	MobileNum = models.IntegerField(unique=True)
	Password = models.CharField(default = "NA",max_length=25)
	city = models.CharField(max_length=50)
	profession = models.CharField(max_length=30)
	def __str__(self):
		return self.Name
class meta:
	models = customer_information
	fields='__all__'
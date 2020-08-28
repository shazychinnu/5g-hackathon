from django.contrib import admin
from .models import customer_information
# Register your models here.

class customerAdmin(admin.ModelAdmin):
	"""docstring for applicationAdmin"""
	list_display = ['registration_time','registration_number','Name','email','gender','address','MobileNum','Password','city','profession']
admin.site.register(customer_information,customerAdmin)




from django.db import models
from django.utils.encoding import smart_unicode

from location_field.models.plain import PlainLocationField


# Create your models here.
class complaint(models.Model):
	name=models.CharField(max_length=120,null=True,blank=True)
	complaint_type=models.CharField(max_length=120,null=True,blank=True)
	complaint_desc=models.CharField(max_length=120,null=True,blank=True)
	address=models.CharField(max_length=120,null=True,blank=True)
	city=models.CharField(max_length=120,null=True,blank=True)
	location = PlainLocationField(based_fields=[city], zoom=7)
	email=models.EmailField()
	number =models.IntegerField()
	timestamp= models.DateTimeField(auto_now_add=True ,auto_now =False)
	updated= models.DateTimeField(auto_now_add=False ,auto_now =True)

	def __unicode__(self):
		return smart_unicode(self.city)
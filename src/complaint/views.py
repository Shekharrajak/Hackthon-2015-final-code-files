from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
# Create your views here.
#from django.contrib import message
from .complaint_form import ComplaintForm
from signups.views import *

def complaint(request):
	form = ComplaintForm(request.POST or None)

	if form.is_valid():
		save_i1t =form.save(commit=False)
		save_it1.save()
		#messages.success(request,'complaint Submitted !')
		return HttpResponseRedirect('/Complaint_registered/')
	return render_to_response("complaint.html",
								locals(),
								context_instance=RequestContext(request))

def complaint_automatic(obj,email_id):
		
		form.name =obj.name
		form.complaint_type =obj.complaint_type
		complaint_type=obj.complaint_type
		form.complaint_desc =obj.complaint_desc
		complaint_desc =obj.complaint_desc
		form.address =obj.address
		form.city =obj.city
		form.location =obj.location
		form.email =obj.email
		form.number=obj.number
		number=obj.number
		# form.name =obj[0]
		# form.complaint_type =obj[1]
		# form.complaint_desc =obj[2]
		# form.address =obj[3]
		# form.city =obj[4]
		#form.location =obj.location
		#form.email =obj[5]
		save_it2 =form.save(commit=False)
		save_it2.save()
		#messages.success(request,'complaint Submitted !')
		#return HttpResponseRedirect('/Complaint_registered/')
		if(complaint_type=='water'):
			send_email('rshekhar@student.nitw.ac.in', 'passwd', 'watermanger@manager.com', 'water problem complaint', complaint_desc,1234567890)
	 	if(complaint_type=='road'):
			send_email('rshekhar@student.nitw.ac.in', 'passwd', 'raod@manager.com', 'road problem complaint', complaint_desc,1234567890)
	 	if(complaint_type=='electricity'):
			send_email('rshekhar@student.nitw.ac.in', 'passwd', 'electricity@manager.com', 'electricity problem complaint', complaint_desc,1234567890)
	 	if(complaint_type=='other'):
			send_email('rshekhar@student.nitw.ac.in', 'passwd', 'other@manager.com', 'other problem complaint', complaint_desc,1234567890)
		#sending mail to complainer about submission
		send_email('rshekhar@student.nitw.ac.in', 'passwd', email_id, 'Complaint submitted and sent to respective department', complaint_desc,number)

def Complaint_registered(request):
	
	return render_to_response("Submitted.html",
								locals(),
								context_instance=RequestContext(request))

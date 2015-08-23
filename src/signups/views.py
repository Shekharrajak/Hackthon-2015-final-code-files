from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
# Create your views here.
from django.contrib import messages
from .forms import SignUpForm
from complaint.views import complaint_automatic
import imaplib

import time
from sinchsms import SinchSMS
import smtplib


def emails_from(name):
    '''Search for all mail from name'''
    status, response = imap_server.search(None, '(FROM "%s")' % name)
    email_ids = [e_id for e_id in response[0].split()]
    print 'Number of emails from %s: %i. IDs: %s' % (name, len(email_ids), email_ids)
    return email_ids

def send_email(user, pwd, recipient, subject, body,Number):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
#sms sending
	# import textmagic.client
	# client = textmagic.client.TextMagicClient('your_username', 'your_api_password')
	# result = client.send("Hello, World!", "1234567890")
	# message_id = result['message_id'].keys()[0]
	number = Number
	message = subject
	client = SinchSMS(your_app_key, your_app_secret)
	# print("Sending '%s' to %s" % (message, number))
	response = client.send_message(number, message)
	message_id = response['MessageId']
	response = client.check_status(message_id)
	while response['Status'] != 'Successful':
		#print(response['Status'])
		#time.sleep(1)
		response = client.check_status(message_id)
		#print(response['Status'])


def get_emails(email_ids):
    		data = []
    		for e_id in email_ids:
    			_, response = imap_server.fetch(e_id, '(UID BODY[TEXT])')
    			data.append(response[0][1])
    		return data

def get_subjects(email_ids):
    subjects = []
    for e_id in email_ids:
        _, response = imap_server.fetch(e_id, '(body[header.fields (subject)])')
        subjects.append( response[0][1][9:] )
    return subjects

def get_complaint_tuple( msg ) :
	prev = 1
	tup = []  
	for i in range(1,len(msg)) : 
		if msg[i] == '#' : 
			tup.append(msg[prev:(i-1)]) 
			prev = i+1 ;
	tup.append(msg[prev:]) 
	return tup ;    


			 
#get_complaint_tuple("#jaye # kjsdh # jsd#khsksdnj #kjsd") ; 


def insert_in_complaint( tup ) : 
	c = Complaint(email_text = tup[0] , type_text = tup[1] , description_text =  tup[2] , address_text = tup[3] , city_text = tup[4] , timestamp_text = timezone.now)
	#c.save()

def home(request):
	obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
	obj.login('username','password')
	obj.select('INBOX')
	count =obj.search(None,'UnSeen')
	status, response = imap.status('INBOX', "(UNSEEN)")
	unreadcount = int(response[0].split()[2].strip(').,]'))

	if(unreadcount):
		# Search for all new mail
		status, email_ids = imap_server.search(None, '(UNSEEN)')
		data = get_emails(email_ids)
		tup=[]
		tup =get_complaint_tuple(data)
		c=insert_in_complaint(tup)
		complaint_automatic(obj,email_ids)




	form = SignUpForm(request.POST or None)

	if form.is_valid():
		save_it =form.save(commit=False)
		save_it.save()
		messages.success(request,'Submitted !')
		return HttpResponseRedirect('/Submitted/')
	return render_to_response("signup.html",
								locals(),
								context_instance=RequestContext(request))

def Submitted(request):
	
	return render_to_response("Submitted.html",
								locals(),
							context_instance=RequestContext(request))


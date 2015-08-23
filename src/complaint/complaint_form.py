from django import forms

from .models import complaint

class ComplaintForm(forms.ModelForm):
	class Meta:
		model=complaint
		fields=['name', 'complaint_type', 'complaint_desc','address','city','email']


		
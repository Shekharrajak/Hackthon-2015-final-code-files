from django.contrib import admin

# Register your models here.
from .models import complaint

class ComplaintAdmin(admin.ModelAdmin):
	class Meta:
		model=complaint
		
admin.site.register(complaint,ComplaintAdmin)

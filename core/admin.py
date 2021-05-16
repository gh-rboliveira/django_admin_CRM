from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Client, Job, Task, Config
from solo.admin import SingletonModelAdmin
from datetime import date    



# Register your models here.
class ClientAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "phone_number")
	def name(self,obj):
		return obj.last_name + ", " + obj.first_name

class TaskInline(admin.TabularInline):
	model = Task
	extra = 0

class JobAdmin(admin.ModelAdmin):
	change_form_template = "admin/job_change_form.html"
	list_display = ("short_description", "status", "link_client", "price")
	list_select_related = (
		'client',
	)
	inlines = [TaskInline]

	def link_client(self, obj):
		link = reverse('admin:core_client_change', args=[obj.client.id])
		return format_html('<a href="{}">{}</a>', link, obj.client.first_name)

	link_client.short_description = 'Client'

class TaskAdmin(admin.ModelAdmin):
	list_display = ("description", "status", "deadline_date", "link_job") #"link_client", 
	list_select_related = (
		'job',
	)
	def link_job(self, obj):
		link = reverse('admin:core_job_change', args=[obj.job.id])
		return format_html('<a href="{}">{}</a>', link, obj.job.short_description)

	link_job.short_description = 'Job'

admin.site.register(Client, ClientAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Config, SingletonModelAdmin)

from django.urls import reverse
from datetime import datetime
from .models import Client, Job, Task

def add_dashboard_data(request):
	"""
	Add data to be used in the dashboard if
	we are in the index of admin page

	Args:
		request ([type]): [description]

	Returns:
		dict: Extra data to be used in the admin page
	"""
	if request.path == reverse("admin:index"):
		num_clients = Client.objects.all().count()
		JobsClosedStatus = ['FINISHED', 'PAYED']
		TasksClosedStatus = ['DONE', 'CANCELED']
		open_jobs = Job.objects.exclude(status__in=JobsClosedStatus).count()

		today = datetime.now()
		overdue_jobs = Job.objects.exclude(status__in=JobsClosedStatus).filter(deadline_date__lt = today).count()
		overdue_tasks = Task.objects.exclude(status__in=TasksClosedStatus).filter(deadline_date__lt = today).count()
		return {
			'num_clients': num_clients,
			'open_jobs': open_jobs,
			'overdue_jobs': overdue_jobs,
			'overdue_tasks': overdue_tasks
		}
	
	return {}
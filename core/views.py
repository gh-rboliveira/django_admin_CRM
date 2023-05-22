from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import Client, Job, Task, Config
from django.shortcuts import get_object_or_404

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class DownloadPDF(View):
	def get(self, request, id):

		job = get_object_or_404(Job, pk=id)
		client = job.client
		tasks = list(job.task_set.all())
		config = Config.objects.get()

		context = {
			"job": job,
			"client": client,
			"tasks": tasks,
			"config": config,
		}

		pdf = render_to_pdf('core/invoice_template.html', context)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice.pdf"
		content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response


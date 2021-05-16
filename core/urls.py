
from django.urls import path
from . import views

urlpatterns = [
     path('pdf/<int:id>', views.DownloadPDF.as_view(), name="pdf_download")

]
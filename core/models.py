from django.db import models
from django.core.validators import RegexValidator
from solo.models import SingletonModel


# Create your models here.
class Client(models.Model):
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDERS)
    email = models.EmailField(max_length=125)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Incorrect Format.Please use: '+999999999' Max 15 Chars.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.TextField(max_length=200, blank=True)
    fiscal_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Job(models.Model):
    STATUS = [
        ('TODO', 'To do'),
        ('ONGOING', 'On going'),
        ('REVIEW', 'In review'),
        ('FINISHED', 'Finished'),
        ('PAYED', 'Payed'),
    ]
    short_description = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default="TODO", choices=STATUS)
    start_date = models.DateField(blank=True, null=True)
    deadline_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.short_description}"

class Task(models.Model):
    STATUS = [
        ('TODO', 'To do'),
        ('ONGOING', 'On going'),
        ('DONE', 'Done'),
        ('CANCELED', 'Canceled'),
    ]
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=10, default="TODO", choices=STATUS)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    deadline_date = models.DateField(blank=True, null=True)
    
class Config(SingletonModel):
    company_name = models.CharField(max_length=200, blank=True, null=True)
    owner_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "CRM Configuration"

    class Meta:
        verbose_name = "CRM Configuration"
from django.db import models

# Create your models here.

class basic_details(models.Model):
    full_name = models.CharField(max_length=200)
    mobile_number = models.IntegerField()
    email_id = models.CharField(max_length=200)
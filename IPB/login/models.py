from django.db import models

# Create your models here.


class details(models.Model):
    username = models.CharField(max_length=15)
    pas = models.CharField(max_length=15)

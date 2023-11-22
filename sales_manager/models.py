from django.db import models

# Create your models here.

from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    office_visited = models.BooleanField(default=False)
    contract_signed = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15)
    sales_channel = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

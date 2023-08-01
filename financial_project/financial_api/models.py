from django.db import models


# Create your models here.

class FinancialData(models.Model):
    # company = models.CharField(max_length=50)
    financial_measure = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField()
    currency = models.CharField(max_length=20)
    unit = models.CharField(max_length=50)

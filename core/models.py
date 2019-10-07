from django.db import models
from django.utils.timezone import now
# Create your models here.

class Purchase(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    address = models.CharField(max_length=20)
    medicine = models.CharField(max_length=120)
    purchase_date = models.DateTimeField(default=now, editable=True)
    clearance_status = models.CharField(max_length=20)
    




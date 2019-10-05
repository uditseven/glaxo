from django.db import models

# Create your models here.

class purchase(models.Model): #name of table

   # id = models.IntegerField(blank=False)
    name = models.CharField(max_length=50, blank=False)
    phone = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return 'Id : {0} Name : {1}',format(self.id, self.name)

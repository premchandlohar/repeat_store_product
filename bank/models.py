from django.db import models

# Create your models here.
class Bankprofile(models.Model):

    state = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=30)
    ifsc_code = models.CharField(max_length=11)
    branch = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    

    def __str__(self):
        return self.bank_name + " :-- " + self.city
    

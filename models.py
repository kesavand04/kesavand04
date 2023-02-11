from django.db import models

# Create your models here.
class NgoDB(models.Model):
    ngo_name = models.CharField(max_length=100)
    ngo_loc =  models.CharField(max_length=100,default="")
    ngo_prevWork = models.CharField(max_length=300,default="")
    ngo_goal = models.CharField(max_length=300,default="")
    ngo_sector = models.CharField(max_length=100)
    ngo_fundingNeeds = models.IntegerField(default=0)

class philDB(models.Model):
    phil_name = models.CharField(max_length=100)
    phil_email = models.CharField(max_length=100)
    phil_phoneNo = models.CharField(max_length=100)
    phil_interest = models.CharField(max_length=300)
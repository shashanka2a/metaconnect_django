from django.db import models

# Create your models here.
class Owner(models.Model):
    owneraddress =  models.CharField(max_length=255,null=True,blank=True)
    moralisid = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.owneraddress



class ProjectDetails(models.Model):
    user = models.ForeignKey(Owner,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True,blank=True)
    symbol = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField()

    def __str__(self):
        return "HELLO"
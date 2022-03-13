from django.db import models

# Create your models here.
class Owner(models.Model):
    owneraddress =  models.CharField(max_length=255,null=True,blank=True)
    moralisid = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.owneraddress



class ProjectDetails(models.Model):
    user = models.ForeignKey(Owner,on_delete=models.CASCADE)
    Name = models.CharField(max_length=255,null=True,blank=True)
    Symbol = models.CharField(max_length=255,null=True,blank=True)
    Description = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Name
    
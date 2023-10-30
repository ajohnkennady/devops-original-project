from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


blood_type=[
    ('A+','a+'),
    ('A-','a-'),
    ('B-','b-'),
    ('B+','b+'),
    ('O+','o+'),
    ('O-','o-'),
    ('AB+','ab+'),
    ('AB-','ab-')

  ]


class Hospital(AbstractUser):
  hospitalname=models.CharField(max_length=200,null=True)
  
  def __str__(self):
    return self.username
  
class Blood(models.Model):
    user = models.ForeignKey(Hospital, on_delete=models.CASCADE,default=None)
    bloodgroupname=models.CharField(choices= blood_type, max_length=5)
    loaction=models.TextField()

    # def __str__(self):
    #     return self.user
  

class Confirmrequest(models.Model):
   userid=models.IntegerField()
   name=models.CharField(max_length=200)
   contact=models.IntegerField()
   bloodgroup=models.CharField(choices= blood_type, max_length=5)
   accept=models.BooleanField(null=True)
  
   def __str__(self):
      return self.name

 
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Blog(models.Model):
    
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=100,null=False)
    content = models.TextField()
    # img = models.ImageField(upload_to='images')
    Img = models.ImageField(upload_to='images/',null=True,blank=True)  
    date_time = models.DateTimeField(auto_now=True,null=True)


    # def __str__(self):
    #     return self.title
    def __str__(self):
        res = super(Blog,self).__str__()
        # print("######################")
        # print("str call in terminal.......")
        return self.title


class Contact(models.Model):
    your_name = models.CharField(max_length=100, null=True)
    your_email = models.EmailField(null=True,unique=True)
    phone = models.IntegerField(max_length=12,null=True)
    # massage = models.CharField(max_length=200,null=True)
    massage = models.TextField(max_length=200, null=True)

    def __str__(self):

        return self.your_email

from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    language = models.CharField(max_length = 200)
    title = models.CharField(max_length = 255)
    overview = models.CharField(max_length = 300)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug  =models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank =True)
    desc = models.TextField(max_length=2000,default= "")
    
    def __str__(self):
        return self.title






class Contact(models.Model):
    msg_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    phone = models.IntegerField(max_length = 70,default="")
    desc = models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name

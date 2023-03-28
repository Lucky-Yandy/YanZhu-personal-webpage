from django.db import models

# Create your models here.

class  Blog(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    image=models.FileField(upload_to="upload", null=True,blank=True)
    
    
    
    
class  Project(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    image=models.FileField(upload_to='upload',  null=True, blank=True)
    field_name = models.URLField(max_length=200)
    
class  AboutMe(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=5000)

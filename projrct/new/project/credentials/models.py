from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250,unique='')
    address=models.TextField()
    img=models.ImageField(upload_to='pics')
    desig=models.CharField(max_length=250)

    def __str__(self):
        return self.name


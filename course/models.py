from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    imgpath = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    def __str__(self):
        return self.adress

class Contact(models.Model):
    CHOICES= ((1, 'phone'), (2,'facebook'), (3, 'email'),)
    type = models.IntegerField(choices=CHOICES)
    value= models.CharField(max_length=255)
    def __str__(self):
        return self.value
  
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey('Category', related_name='courses', on_delete=models.DO_NOTHING)
    logo = models.CharField(max_length=255)
    contacts = models.ForeignKey('Contact', related_name='courses', on_delete=models.DO_NOTHING)
    branches = models.ForeignKey('Branch', related_name='courses', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name    
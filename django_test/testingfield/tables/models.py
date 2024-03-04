from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

class car(models.Model):
    car_name = models.CharField(max_length=100, default = 1)
    car_age = models.IntegerField(default=2)


    def __str__(self) -> str:
        return self.car_name
    
from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, unique=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    DOB = models.DateField()
    GenderType = models.TextChoices("Gender", "Female Male")
    gender = models.CharField(choices=GenderType.choices, max_length=10, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True,)

    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name
    
from django.contrib import admin
from .models import Country, City, Skill, Employee

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Skill)
admin.site.register(Employee)

# Generated by Django 4.2.2 on 2023-08-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_alter_employee_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('0', 'Male'), ('1', 'Female')], max_length=10),
        ),
    ]

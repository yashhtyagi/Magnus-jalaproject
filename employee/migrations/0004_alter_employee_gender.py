# Generated by Django 4.2.2 on 2023-08-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_rename_skills_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, choices=[('0', 'Male'), ('1', 'Female')], max_length=10),
        ),
    ]

from django.db import models

# Create your models here.

class ImageUpload(models.Model):

    image = models.ImageField(upload_to="static/image/", blank=True, null=True)
    image_des =models.CharField( max_length=500, blank=True, null=True)

    def __str__(self):
        return self.image_des
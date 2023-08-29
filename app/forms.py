from django import forms
from .models import ImageUpload

class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageUpload
        fields = ('image', 'image_des')


        widgets = {
            'image' : forms.FileInput(attrs={'class': 'form-control','required': ''}),
            'image_des' : forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
        }
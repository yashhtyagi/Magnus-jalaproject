from .models import Employee, City
from django import forms

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'mobile', 'DOB', 'gender', 'address', 'country', 'city', 'skills')

        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend2', 'required': ''}),
            'mobile' : forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
            'DOB' : forms.DateInput(attrs={'class': 'form-control', 'required': '', 'type':'date'}),
            'gender' : forms.RadioSelect(),
            'address' : forms.Textarea(attrs={'class': 'form-control','rows':'3', 'required': ''}),
            'country' : forms.Select(attrs={'class': 'form-control', 'required': ''}),
            'city' : forms.Select(attrs={'class': 'form-control', 'required': ''}),
            'skills' : forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
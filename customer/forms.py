from django import forms
from django.forms import ModelForm
from staff.models import Customer
class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields=['first_name', 'last_name', 'national_id_front', 'national_id_back', 'phone', 'email']

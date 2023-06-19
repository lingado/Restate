from django import forms
from django.forms import ModelForm
from staff.models import *


class HouseForm(ModelForm):
    class Meta:
        model=House
        fields=['name','location']

class HouseAmenityForm(ModelForm):
    class Meta:
        model=HouseAmenity
        fields=['house','amenity']

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields=['first_name', 'last_name', 'national_id_front', 'national_id_back', 'phone', 'email', 'profile_img']

class HouseRatingForm(ModelForm):
    class Meta:
        model=HouseRating
        fields=['customer','house', 'rating', 'comment']

class HouseTypeForm(ModelForm):
    class Meta:
        model=HouseType
        fields='__all__'

class Amenities(ModelForm):
    class Meta:
        model=Amenities
        fields='__all__'




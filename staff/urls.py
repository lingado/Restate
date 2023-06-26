from django.urls import path
from .views import  *
app_name="staff"
urlpatterns=[
    path('dashboard/', dashboard, name="dashboard"),
    path('houses/',houses, name="houses"),
    path('customer/',customer, name="customer"),
    path('location/', location, name="location"),
    path('housetype/', housetypes, name="house-type"),
    path('location/houses/<location_id>',location_houses, name="location-houses"),
    path('location/house/<location_id>/<property_id>', house_location_details, name="house-location")

]
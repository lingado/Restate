from django.urls import path
from .views import *

app_name="customer"
urlpatterns = [
    path('', index, name="index"),
    path('house-categories/',house_types, name="houses"),
    path('properties/',properties, name="properties"),
    path('contacts/',contacts, name="contacts"),
    path('submit-message/',submit_message, name="submit-message"),
    path('houses/details/<property_id>',property_details, name="property-details"),
    path('house-categories/houses/<category_id>',houses_in_category, name="house-categories-details")

]

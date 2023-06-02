from django.urls import path
from .views import *

app_name="customer"
urlpatterns = [
    path('', index, name="index"),
    path('houses/',house, name="house"),
    path('properties/',properties, name="properties"),
    path('contacts/',contacts, name="contacts"),
    path('submit-message/',submit_message, name="submit-message")
]

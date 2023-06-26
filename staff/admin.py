from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(HouseType)
admin.site.register(House)
admin.site.register(Location)
admin.site.register(Amenities)
admin.site.register(HouseAmenity)
admin.site.register(HouseRating)
admin.site.register(Message)

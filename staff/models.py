from django.db import models

# Create your models here.
class Amenities(models.Model):
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='media/amenities', null=True, blank=T)


class HOuseType(models.Model):
    RENTAL=1
    MORTGAGE=2

    TYPE_CHOICES = (
        (RENTAL, "Rental"),
        (MORTGAGE, "Mortgage")
    )

    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='media/house_types')
    choices= models.IntegerField(choices=TYPE_CHOICES)

class Location(models.Model):
    COUNTY_CHOICES = (
        (001, "Mombasa"),
        (003, "Kilifi"),
        (022, "Kiambu"),
        (042, "Kisumu"),
        (032, "Nakuru"),
        (047, "Nairobi"),
        
    )
    county= models.IntegerField(choices=COUNTY_CHOICES)
    name= models.CharField(max_length=100)

class House(models.Model):
    AVAILABLE = 1
    UNAVAILABLE = 2
    STATUS_CHOICES = (
        (AVAILABLE, "Available"),
        (UNAVAILABLE, "Unavailable")
    )
    name= models.CharField(max_length=100)
    price= models.DecimalField()
    Location= models.ForeignKey(Location, on_delete=models.PROTECT)
    image= models.ImageField(upload_to='media/houses')
    house_type = models.ForeignKey(HOuseType, on_delete=models.PROTECT)
    number_of_rooms= models.IntegerField()
    status= models.IntegerField(choices=STATUS_CHOICES)

class HouseAmenity(models.Model):
    house= models.ForeignKey(House, on_delete=models.CASCADE)
    amenity= models.ForeignKey(Amenities, null=True, blank=True, on_delete=models.SET_NULL)

class Customer(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    national_id_front= models.ImageField(upload_to='media/ ')
    national_id_back= models.ImageField(upload_to='media/ ')
    phone= models.IntegerField()
    profile_img= models.ImageField(upload_to='media/ ')

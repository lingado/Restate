from django.db import models

# Create your models here.
class Amenities(models.Model):
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='amenities', null=True, blank=True)

    class Meta:
        verbose_name_plural= "Amenities"

    def __str__(self):
        return self.name


class HouseType(models.Model):
    RENTAL=1
    MORTGAGE=2

    TYPE_CHOICES = (
        (RENTAL, "Rental"),
        (MORTGAGE, "Mortgage")
    )

    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='house_types')
    choices= models.IntegerField(choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name
class Location(models.Model):
    COUNTY_CHOICES = (
        (1, "Mombasa"),
        (3, "Kilifi"),
        (22, "Kiambu"),
        (42, "Kisumu"),
        (32, "Nakuru"),
        (47, "Nairobi"),
        (21, "Murang'a"), 
        (2, "Kwale"),
        (5, "Lamu"),
        
    )
    county= models.IntegerField(choices=COUNTY_CHOICES)
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class House(models.Model):
    AVAILABLE = 1
    UNAVAILABLE = 2
    STATUS_CHOICES = (
        (AVAILABLE, "Available"),
        (UNAVAILABLE, "Unavailable")
    )
    name= models.CharField(max_length=100)
    price= models.DecimalField(decimal_places=2, max_digits=15)
    Location= models.ForeignKey(Location, on_delete=models.PROTECT)
    image= models.ImageField(upload_to='houses')
    house_type = models.ForeignKey(HouseType, on_delete=models.PROTECT)
    number_of_rooms= models.IntegerField()
    status= models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

class HouseAmenity(models.Model):
    house= models.ForeignKey(House, on_delete=models.CASCADE)
    amenity= models.ForeignKey(Amenities, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural= "House Amenities"

    def __str__(self):
        return self.house.name

class Customer(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    national_id_front= models.ImageField(upload_to='id_front')
    national_id_back= models.ImageField(upload_to='id_back')
    phone= models.IntegerField()
    email= models.EmailField()
    profile_img= models.ImageField(upload_to='profile_photos')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class HouseRating(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    comment = models.TextField()

    def __str__(self):
        return self.house.name

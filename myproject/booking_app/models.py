from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Country(models.Model):
    country_name = models.CharField(max_length=32,unique=True)
    country_image = models.ImageField(upload_to='images_country/')

    def __str__(self):
        return self.country_name


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(80)],
                                           null=True, blank=True)
    user_image = models.ImageField(upload_to='user_photo/', null=True, blank=True)
    phone_number = PhoneNumberField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    RoleChoices=(
    ('owner', 'owner'),
    ('client', 'client')
    )
    role = models.CharField(max_length=32, choices=RoleChoices, default='client')
    data_registration = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.role}'


class City(models.Model):
    city_name = models.CharField(max_length=32, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_image = models.ImageField(upload_to='city_photo/')

    def __str__(self):
        return self.city_name


class Service(models.Model):
    service_name = models.CharField(max_length=32, unique=True)
    service_image = models.ImageField(upload_to='service_image/')

    def __str__(self):
        return self.service_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotel_city')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    postal_code = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=100)
    hotel_stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField()
    service  = models.ManyToManyField(Service)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_photo')
    hotel_image = models.ImageField(upload_to='image_hotel/')



class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_room')
    room_number = models.IntegerField()
    Type_Choices = (
    ('люкс', 'люкс'),
    ('полулюкс', 'полулюкс'),
    ('эконом', 'эконом'),
    ('семейный', 'семейный'),
    ('одноместный', 'одноместный'),
    )
    room_type = models.CharField(max_length=32, choices=Type_Choices)
    Status_Choices = (
    ('Занят', 'Занят'),
    ('Свободный', 'Свободный'),
    ('Забронирован', 'Забронирован'),
    )
    status_room = models.CharField(max_length=32, choices=Status_Choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_description = models.TextField()

    def __str__(self):
        return f'{self.status_room} {self.room_number}'


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_photo')
    room_image = models.ImageField(upload_to='room_photo/')



class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_review')
    text = models.TextField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(choices=[(i,str(i)) for i in range (1,11)], null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} {self.user.username} {self.hotel.hotel_name}'



class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} {self.hotel} {self.room}'

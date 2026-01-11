from rest_framework import serializers
from .models import (Country,UserProfile,City,
                     Service,Hotel,HotelImage,
                     Room,RoomImage,Review,Booking)

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountryNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name',]



class CountrySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name','country_image']


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    country = CountrySimpleSerializers()
    class Meta:
        model = UserProfile
        fields = ['id','username','user_image','country']



class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','city_name','city_image']


class CityNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name', ]


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image',]


class HotelListSerializers(serializers.ModelSerializer):
    hotel_photo = HotelImageSerializers(many=True, read_only=True)
    city = CityNameSerializers()
    country = CountryNameSerializers()
    class Meta:
        model = Hotel
        fields = ['id','hotel_photo','hotel_name','city','country']



class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'



class CityDetailSerializers(serializers.ModelSerializer):
    hotel_city = HotelListSerializers(many=True, read_only=True)
    class Meta:
        model = City
        fields = ['city_name','hotel_city']



class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_name','service_image']




class RoomListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','room_number','room_type',
                  'status_room','price','room_description']

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'



class ReviewListSerializers(serializers.ModelSerializer):
    user = UserProfileSimpleSerializers()
    class Meta:
        model = Review
        fields = ['user','text']


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
            model = Review
            fields = '__all__'


class ReviewDetailSerializers(serializers.ModelSerializer):
    user = UserProfileSimpleSerializers()
    class Meta:
        model = Review
        fields = ['id','user','hotel','text','created_date','rating']



class HotelDetailSerializers(serializers.ModelSerializer):
    hotel_photo = HotelImageSerializers(many=True, read_only=True)
    city = CityNameSerializers()
    country = CountryNameSerializers()
    service = ServiceSerializers(many=True)
    owner = UserProfileNameSerializers()
    hotel_room = RoomListSerializers(many=True, read_only=True)
    hotel_review = ReviewListSerializers(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['hotel_name','hotel_photo','city','country','postal_code',
                  'street','hotel_stars','description','service','owner','hotel_room','hotel_review']



class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomDetailSerializers(serializers.ModelSerializer):
    room_photo = RoomImageSerializers(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'hotel','room_photo', 'room_number', 'room_type',
                  'status_room', 'price', 'room_description']



class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
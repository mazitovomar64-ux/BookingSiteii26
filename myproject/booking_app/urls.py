from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (RegisterView,LogoutView,LoginView,CountryViewSet,UserProfileViewSet,CityListAPIView,CityDetailAPIView,
                    ServiceViewSet,HotelListAPIView,HotelDetailAPIView,
                    ReviewListAPIView,ReviewDetailAPIView,RoomListAPIView,RoomDetailAPIView,
                    BookingViewSet,ReviewCreateAPIView,ReviewEditAPIView,RoomCreateAPIView,RoomEditAPIView,
                    HotelCreateAPIView,HotelEditAPIView)

router = DefaultRouter()


router.register('countries', CountryViewSet)
router.register('users', UserProfileViewSet)
router.register('services', ServiceViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('hotel/create/', HotelCreateAPIView.as_view(), name='hotel_create'),
    path('hotel/<int:pk>/edit/', HotelEditAPIView.as_view(), name='hotel_edit'),
    path('room/', RoomListAPIView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('room/create/', RoomCreateAPIView.as_view(), name='room_create'),
    path('room/<int:pk>/edit', RoomEditAPIView.as_view(), name='room_edit'),
    path('review/', ReviewListAPIView.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review_detail'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('review/<int:pk>/edit/', ReviewEditAPIView.as_view(), name='review_edit'),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
]
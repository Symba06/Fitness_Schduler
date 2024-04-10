from django.urls import path
from . import views
from .views import UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('users/', views.UserListCreateAPIView.as_view(), name='list-users'),
    path('trainers/', views.TrainerListCreateAPIView.as_view(), name='list-trainers'),
    path('rooms/', views.RoomListCreateAPIView.as_view(), name='list-rooms'),
    path('schedules/', views.ScheduleListCreateAPIView.as_view(), name='list-schedules'),
    path('bookings/', views.BookingListCreateAPIView.as_view(), name='list-bookings'),
]

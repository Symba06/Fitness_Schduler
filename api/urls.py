from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersApiView.as_view(), name='list-users'),
    path('trainers/', views.TrainerApiView.as_view(), name='list-trainers'),
    path('rooms/', views.RoomApiView.as_view(), name='list-rooms'),
    path('schedules/', views.ScheduleApiView.as_view(), name='list-schedules'),
    path('bookings/', views.BookingApiView.as_view(), name='list-bookings'),
]

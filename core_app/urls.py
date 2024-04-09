from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('trainers/', views.TrainerListView.as_view(), name='trainer-list'),
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('schedules/', views.ScheduleListView.as_view(), name='schedule-list'),
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),
]

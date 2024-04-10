from django.urls import path
from . import views
from .swagger import schema_view

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('trainers/', views.TrainerListView.as_view(), name='trainer-list'),
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('schedules/', views.ScheduleListView.as_view(), name='schedule-list'),
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

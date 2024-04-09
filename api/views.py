from rest_framework.generics import ListAPIView
from . serializers import UserSerializer, TrainerSerializer, RoomSerializer, ScheduleSerializer, BookingSerializer
from core_app.models import CustomUser, Trainer, Room, Schedule, Booking

class UsersApiView(ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class TrainerApiView(ListAPIView):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()


class RoomApiView(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class ScheduleApiView(ListAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

class BookingApiView(ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

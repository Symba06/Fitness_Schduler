from .models import Trainer, Schedule, Booking, Room
from django.views.generic import ListView
from .models import CustomUser


class UserListView(ListView):
    model = CustomUser

    def get_queryset(self):
        if self.request.user.is_superuser:
            return CustomUser.objects.all()
        elif self.request.user.role == 'trainer':
            return CustomUser.objects.filter(role='client')
        else:
            return CustomUser.objects.filter(id=self.request.user.id)

class TrainerListView(ListView):
    model = Trainer

    def get_queryset(self):
        queryset = super().get_queryset()
        gender_filter = self.request.GET.get('gender')
        if gender_filter:
            queryset = queryset.filter(gender=gender_filter)
        return queryset


class RoomListView(ListView):
    model = Room

    def get_queryset(self):
        qs = Room.objects.all()
        return qs


class ScheduleListView(ListView):
    model = Schedule

    def get_queryset(self):
        trainer_id = self.request.GET.get('trainer_id')
        if trainer_id:
            return Schedule.objects.filter(trainer_id=trainer_id)
        else:
            return Schedule.objects.all()

class BookingListView(ListView):
    model = Booking

    def get_queryset(self):
        qs = Booking.objects.all()
        return qs

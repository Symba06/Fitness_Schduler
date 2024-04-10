from .models import Trainer, Schedule, Booking, Room
from django.views.generic import ListView
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model


class UserListView(ListView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                users = get_user_model().objects.all()
            elif request.user.role == 'trainer':
                users = get_user_model().objects.filter(role='client')
            else:
                users = get_user_model().objects.filter(id=request.user.id)
            data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': 'Authentication required'}, status=401)


class TrainerListView(ListView):
    model = Trainer

    def get(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        gender_filter = request.GET.get('gender')

        if gender_filter:
            trainers = queryset.filter(gender=gender_filter)
        else:
            trainers = queryset.all()

        data = [{'id': trainer.id, 'name': trainer.full_name, 'gender': trainer.gender, 'fitness_room': trainer.fitness_rooms} for trainer in trainers]
        return JsonResponse(data, safe=False)

class RoomListView(ListView):
    model = Room

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()

        data = [{'id': room.id, 'name': room.name, 'capacity': room.capacity} for room in rooms]
        return JsonResponse(data, safe=False)


class ScheduleListView(ListView):
    model = Schedule

    def get(self, request, *args, **kwargs):
        schedules = Schedule.objects.all()

        data = []
        for schedule in schedules:
            schedule_data = {
                'id': schedule.id,
                'trainer_id': schedule.trainer.id if schedule.trainer else None,
                'trainer_name': schedule.trainer.full_name if schedule.trainer else None,
                'room_id': schedule.room.id if schedule.room else None,
                'start_time': schedule.start_time,
                'end_time': schedule.end_time
            }
            data.append(schedule_data)

        return JsonResponse(data, safe=False)

# class BookingListView(ListView):
#     model = Booking
#
#     def get(self, request, *args, **kwargs):
#         bookings = Booking.objects.all()
#
#         data = [{'id': booking.id, 'user_id': booking.user_id, 'room_id': booking.room_id, 'start_time': booking.start_time, 'end_time': booking.end_time} for booking in bookings]
#         return JsonResponse(data, safe=False)

class BookingListView(ListView):
    model = Booking

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.all()

        data = []
        for booking in bookings:
            booking_data = {
                'id': booking.id,
                'user_id': booking.user.id,
                'user_username': booking.user.username,
                'trainer_id': booking.trainer.id if booking.trainer else None,
                'trainer_name': booking.trainer.full_name if booking.trainer else None,
                'room_id': booking.room.id,
                'start_time': booking.start_time,
                'end_time': booking.end_time
            }
            data.append(booking_data)

        return JsonResponse(data, safe=False)
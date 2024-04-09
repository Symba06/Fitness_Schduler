from rest_framework import serializers
from core_app.models import CustomUser, Trainer, Schedule, Booking, Room

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'phone', 'role',)

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'
        read_only_fields = ['fitness_rooms']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'trainer', 'schedule', 'date_and_time']
        read_only_fields = ['id']


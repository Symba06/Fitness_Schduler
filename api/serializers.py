from rest_framework import serializers
from core_app.models import CustomUser, Trainer, Schedule, Booking, Room

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)

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
    trainer_name = serializers.SerializerMethodField()
    room_number = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id', 'user_id', 'trainer_id', 'schedule_id', 'booking_datetime', 'start_time', 'end_time', 'trainer_name', 'room_number']

    def get_trainer_name(self, obj):
        return obj.trainer.full_name if obj.trainer else None

    def get_room_number(self, obj):
        return obj.room.room_number if obj.room else None
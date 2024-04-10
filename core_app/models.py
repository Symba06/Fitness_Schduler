from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta

class CustomUser(AbstractUser):
    ROLES = (
        ('client', 'Client'),
        ('trainer', 'Trainer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLES)
    email = models.EmailField("Email", unique=True, max_length=255)
    username = models.CharField("Username", unique=True, max_length=255)
    phone = models.CharField("Phone", max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Trainer(models.Model):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDERS)
    fitness_rooms = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

    def __str__(self):
        return self.full_name

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    capacity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Фитнесс залы'
        verbose_name_plural = 'Фитнесс залы'


class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    date_and_time = models.DateTimeField(default=datetime.now)
    duration = models.DurationField(default=timedelta(hours=1))
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

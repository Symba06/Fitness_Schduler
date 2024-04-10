# Fitness_Scheduler

This project is a Django-based web application designed to manage the schedules of fitness trainers.

## Description

The Fitness Scheduler Project provides a platform for managing the schedules of fitness trainers, clients, and administrative users. It allows trainers to set their availability, clients to book appointments with trainers, and administrators to manage users, trainers, rooms, and schedules.

## Features

- User registration and authentication with role-based access control (client, trainer, admin)
- User management (CRUD operations for users, trainers, and clients)
- Trainer management (CRUD operations for trainers)
- Room management (CRUD operations for fitness rooms)
- Schedule management (CRUD operations for trainer schedules)
- Booking management (CRUD operations for user bookings)
  
## API Endpoints

The following endpoints are available:

/api/users/: User management (GET, POST)
/api/trainers/: Trainer management (GET, POST)
/api/rooms/: Room management (GET, POST)
/api/schedules/: Schedule management (GET, POST)
/api/bookings/: Booking management (GET, POST)
/api/auth/register/: User registration (POST)
/api/auth/login/: User login (POST)

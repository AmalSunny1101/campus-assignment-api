# Campus Assignment Management API

## Overview
This is a RESTful API developed for managing student assignments.
Students can register, login, and manage assignments securely.

## Tech Stack
- Django REST Framework
- JWT Authentication
- SQLite/MySQL Database
- Python

## Setup Instructions

1. Clone repository:
git clone <your-repo-link>

2. Install dependencies:
pip install -r requirements.txt

3. Apply migrations:
python manage.py migrate

4. Run server:
python manage.py runserver

## API Endpoints

### Authentication
POST /api/register/
POST /api/login/

### Assignments
POST /api/assignments/
GET /api/assignments/
PUT /api/assignments/{id}/
DELETE /api/assignments/{id}/

## Sample Login Request
{
 "username": "rahul",
 "password": "rahul123"
}

## Postman Collection
Included in repository.
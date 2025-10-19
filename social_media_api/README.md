# Social Media API - User Authentication Setup

## Overview
This project initializes a Django REST Framework-based social media API, implementing a custom user model and token-based authentication.

## Features
- Custom user model (bio, profile picture, followers)
- User registration and login
- Token-based authentication (DRF TokenAuth)
- Authenticated user profile management

## Endpoints
| Endpoint |             Method |                    Description |
|-----------|--------|--------------|
| `/api/accounts/register/` | POST | Register a new user |
| `/api/accounts/login/` | POST | Log in and retrieve authentication token |
| `/api/accounts/profile/` | GET/PUT | Retrieve or update authenticated user profile |

## Setup
```bash
pip install django djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Social Media API - User Authentication Setup

## Overview
This project initializes a Django REST Framework-based social media API, implementing a custom user model and token-based authentication.


## accounts Features
- Custom user model (bio, profile picture, followers)
- User registration and login
- Token-based authentication (DRF TokenAuth)
- Authenticated user profile management

## accounts Endpoints
| Endpoint |             Method |                    Description |
|-----------|--------|--------------|
| `/api/accounts/register/` | POST | Register a new user |
| `/api/accounts/login/` | POST | Log in and retrieve authentication token |
| `/api/accounts/profile/` | GET/PUT | Retrieve or update authenticated user profile |

## POSTS ENDPOINTS
Method	Endpoint	Description	Auth Required
GET	/posts/	Retrieve all posts (paginated)	❌ No
GET	/posts/{id}/	Retrieve a single post	❌ No
POST	/posts/	Create a new post	✅ Yes
PUT/PATCH	/posts/{id}/	Update a post (owner only)	✅ Yes
DELETE	/posts/{id}/	Delete a post (owner only)	✅ Yes
Example Request (Create Post)
POST /api/posts/
{
  "title": "My First Post",
  "content": "This is my first post content."
}

Example Response
{
  "id": 1,
  "author": "fridah",
  "title": "My First Post",
  "content": "This is my first post content.",
  "created_at": "2025-10-19T20:21:12Z",
  "updated_at": "2025-10-19T20:21:12Z",
  "comments": []
}

COMMENTS ENDPOINTS
Method	Endpoint	Description	Auth Required
GET	/comments/	Retrieve all comments	❌ No
GET	/comments/{id}/	Retrieve a specific comment	❌ No
POST	/comments/	Create a new comment	✅ Yes
PUT/PATCH	/comments/{id}/	Update a comment (owner only)	✅ Yes
DELETE	/comments/{id}/	Delete a comment (owner only)	✅ Yes
Example Request (Create Comment)
POST /api/comments/
{
  "post": 1,
  "content": "This is an awesome post!"
}

Example Response
{
  "id": 3,
  "post": 1,
  "author": "fridah",
  "content": "This is an awesome post!",
  "created_at": "2025-10-19T21:40:12Z",
  "updated_at": "2025-10-19T21:40:12Z"
} 

## Setup
```bash
pip install django djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

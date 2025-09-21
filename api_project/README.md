### 🔐 Authentication Setup
This project uses **Token Authentication** with Django REST Framework.

- Obtain a token:
  ```bash
  POST /api/token/
  {
    "username": "your_username",
    "password": "your_password"
  }

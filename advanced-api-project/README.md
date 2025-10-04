# 📘 Advanced API Project - Django REST Framework

## Overview
This project extends the **Advanced API Project** by implementing **custom views** and **generic views** using Django REST Framework (DRF).  
The goal is to efficiently handle CRUD operations for the `Book` model while applying custom behavior, permissions, and validation logic.

---

## 🧩 Features Implemented

### ✅ CRUD Operations via Generic Views
We used DRF’s **generic class-based views** to perform Create, Read, Update, and Delete operations on the `Book` model.

| View Class | HTTP Method(s) | Endpoint | Description |
|-------------|----------------|-----------|--------------|
| `BookListCreateView` | `GET`, `POST` | `/api/books/` | Lists all books or creates a new one |
| `BookRetrieveUpdateDestroyView` | `GET`, `PUT`, `DELETE` | `/api/books/<int:pk>/` | Retrieves, updates, or deletes a specific book |

---

## 🛠️ View Configurations

### 1️⃣ `BookListCreateView`
- Inherits from `generics.ListCreateAPIView`
- Handles:
  - **GET:** Retrieve all `Book` instances
  - **POST:** Create a new book (requires authentication)
- Custom permission logic:
  ```python
  def get_permissions(self):
      if self.request.method == 'GET':
          return [permissions.AllowAny()]
      return [permissions.IsAuthenticated()]

### Filtering, Searching, and Ordering

This API supports advanced query capabilities on the `/books/` endpoint.

#### Filtering
Filter books by title, author, or publication year:

## 🧪 API Testing

All API tests are located in `api/test_views.py`.  
They cover:
- CRUD operations for the `Book` model
- Filtering, Searching, and Ordering
- Permission and authentication checks

### Running Tests

Use Django’s test runner:

```bash
python manage.py test api

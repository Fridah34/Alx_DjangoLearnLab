# Advanced API Project – Custom Serializers in Django REST Framework

## 📌 Objective
This project sets up a Django REST Framework (DRF) project that demonstrates the use of **custom serializers** to handle **nested relationships** and **custom validation rules**.  

The focus is on modeling `Author` and `Book` entities, with serializers that can return nested book data for each author and enforce validation constraints.

---

## 🚀 Features
- Django + Django REST Framework setup
- Models:
  - `Author` (with `name` field)
  - `Book` (with `title`, `publication_year`, and foreign key to Author)
- Custom Serializers:
  - `BookSerializer` with validation (publication year cannot be in the future)
  - `AuthorSerializer` that nests related books using `BookSerializer`
- One-to-many relationship between Authors and Books
- Tested using Django shell and Admin interface

---

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/advanced-api-project

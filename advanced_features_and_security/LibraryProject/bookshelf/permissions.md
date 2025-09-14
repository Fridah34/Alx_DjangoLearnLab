# Django Permissions and Groups

## Overview
This project demonstrates how to implement **custom permissions** and manage **user groups** in Django.

---

## 1. Custom Permissions in Models
Defined in `bookshelf/models.py` inside the `Book` model:

- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

---

## 2. Groups and Roles
Configured in the **Django Admin**:

- **Viewers** → `can_view`
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Admins** → all permissions

---

## 3. Views with Permission Checks
In `bookshelf/views.py`, we use decorators like:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)

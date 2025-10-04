from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITests(APITestCase):
    """✅ Unit tests for Book API endpoints."""

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Create an author
        self.author = Author.objects.create(name="John Doe", biography="A test author")

        # Create some books
        self.book1 = Book.objects.create(title="Book One", author=self.author, publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author=self.author, publication_year=2021)

        # API client
        self.client = APIClient()

        # URLs
        self.list_url = reverse("book-list")   # ✅ Should match your BookListView route
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    def test_list_books(self):
        """✅ Test listing all books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_filter_books_by_title(self):
        """✅ Test filtering books by title."""
        response = self.client.get(self.list_url, {"title": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books_by_author(self):
        """✅ Test searching books by author name."""
        response = self.client.get(self.list_url, {"search": "John"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books_by_publication_year(self):
        """✅ Test ordering books by publication year."""
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("publication_year", response.data[0])

    def test_create_book_authenticated(self):
        """✅ Authenticated user can create a book."""
        self.client.login(username="testuser", password="testpassword")
        data = {"title": "New Book", "author": self.author.id, "publication_year": 2025}
        response = self.client.post(reverse("book-create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """❌ Unauthenticated users cannot create books."""
        data = {"title": "Unauthorized Book", "author": self.author.id, "publication_year": 2024}
        response = self.client.post(reverse("book-create"), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """✅ Authenticated user can update a book."""
        self.client.login(username="testuser", password="testpassword")
        data = {"title": "Updated Book Title"}
        response = self.client.patch(reverse("book-update", args=[self.book1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book Title")

    def test_delete_book(self):
        """✅ Authenticated user can delete a book."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(reverse("book-delete", args=[self.book2.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Author model:
    - name: stores the author's full name.
    - related_name 'books' used so we can access author.books.all() in serializers.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    - title: the book title.
    - publication_year: integer year the book was published.
    - author: FK to Author (one Author -> many Books).
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
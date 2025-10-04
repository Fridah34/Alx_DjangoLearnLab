# api/serializers.py
from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    - Serializes all fields of Book.
    - Adds validation to prevent a future publication_year.
    """
    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year', 'author')  # author is id by default

    def validate_publication_year(self, value):
        """
        Ensure publication_year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    - Includes 'name' and a nested list of this author's books.
    - `books` uses BookSerializer (read-only) to show nested data dynamically.
    """
    books = BookSerializer(many=True, read_only=True)  # related_name='books' on FK

    class Meta:
        model = Author
        fields = ('id', 'name', 'books')

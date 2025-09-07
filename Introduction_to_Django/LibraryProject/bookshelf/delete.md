from bookshelf.models import Book

# Delete the book
book = Book.objects.first()
book.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>
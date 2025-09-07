from bookshelf.models import Book

# Get the book and update its title
book = Book.objects.first()
book.title = \"Nineteen Eighty-Four\"
book.save()

book
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
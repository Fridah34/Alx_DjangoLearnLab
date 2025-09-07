from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
books
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Access the first book
book = books.first()
book.title
# '1984'
book.author
# 'George Orwell'
book.publication_year
# 1949
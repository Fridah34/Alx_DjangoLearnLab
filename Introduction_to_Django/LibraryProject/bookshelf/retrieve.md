from bookshelf.models import Book

# Retrieve all books
book = Book.objects.get(title="1984")
book
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Access the first book
book.title
# '1984'
book.author
# 'George Orwell'
book.publication_year
# 1949
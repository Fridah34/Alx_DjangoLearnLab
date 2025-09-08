## 1. Create
\`\`\`python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell (1949)>
\`\`\`

## 2. Retrieve
\`\`\`python
books = Book.objects.get(title="1984")
books
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

book = books.first()
book.title
# '1984'
book.author
# 'George Orwell'
book.publication_year
# 1949
\`\`\`

## 3. Update
\`\`\`python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
\`\`\`

## 4. Delete
\`\`\`python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
# <QuerySet []>
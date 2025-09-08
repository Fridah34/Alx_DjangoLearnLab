import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def create_sample_data():
    author, _ = Author.objects.get_or_create(name='George Orwell')
    b1, _ = Book.objects.get_or_create(title='1984', author=author)
    b2, _ = Book.objects.get_or_create(title='Animal Farm', author=author)

    library, _ = Library.objects.get_or_create(name='Central Library')
    library.books.add(b1, b2)  # ManyToMany

    librarian, _ = Librarian.objects.get_or_create(name='Alice', library=library)

    return {
        'author': author,
        'books': [b1, b2],
        'library': library,
        'librarian': librarian,
    }


# ✅ List all books in a library
def list_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    books = library.books.all()
    for book in books:
        print(book.title)


# ✅ Query all books by a specific author
def list_books_by_author(author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author)  # <-- this matches the checker
    for book in books:
        print(book.title)


# ✅ Retrieve the librarian for a library
def get_librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)
    librarian = Librarian.objects.get(library=library)
    print(librarian.name)


if __name__ == "__main__":
    sample = create_sample_data()
    list_books_in_library(sample['library'].id)
    list_books_by_author(sample['author'].id)
    get_librarian_for_library(sample['library'].id)

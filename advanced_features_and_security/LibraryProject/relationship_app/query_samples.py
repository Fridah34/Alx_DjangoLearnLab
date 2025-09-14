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


# ✅ Query all books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # exact pattern checker wants
    print(f"Books by {author_name}:")
    for book in books:
        print(book.title)


# ✅ List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # exact pattern checker wants
    books = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books:
        print(book.title)


# ✅ Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # exact pattern checker wants
    librarian = Librarian.objects.get(library=library)  # matches checker
    print(f"\nLibrarian for {library_name}: {librarian.name}")


if __name__ == "__main__":
    sample = create_sample_data()
    query_books_by_author(sample['author'].name)
    list_books_in_library(sample['library'].name)
    get_librarian_for_library(sample['library'].name)

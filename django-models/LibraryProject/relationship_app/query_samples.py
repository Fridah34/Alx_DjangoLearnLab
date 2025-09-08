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
    # add books to library (ManyToMany)
    library.books.add(b1, b2)

    librarian, _ = Librarian.objects.get_or_create(name='Alice', library=library)

    return {
        'author': author,
        'books': [b1, b2],
        'library': library,
        'librarian': librarian,
    }

def query_books_by_author(author_name):
    # Option A: via Book filter
    books = Book.objects.filter(author__name=author_name)
    print(f"Books by {author_name} (via Book.objects.filter):")
    for b in books:
        print(" -", b)

    # Option B: via Author instance
    try:
        author = Author.objects.get(name=author_name)
        print(f"\nBooks via author.books.all():")
        for b in author.books.all():
            print(" -", b)
    except Author.DoesNotExist:
        print("Author not found:", author_name)

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print("Library not found:", library_name)
        return
    print(f"\nBooks in library '{library.name}':")
    for b in library.books.all():
        print(" -", b)

def get_librarian_for_library(library_name):
    try:
        # Option A: via related_name from Library
        library = Library.objects.get(name=library_name)
        if hasattr(library, 'librarian'):
            print(f"\nLibrarian for '{library.name}' (via library.librarian): {library.librarian}")
        else:
            print(f"\nNo librarian set for library {library.name}")

        # Option B: query Librarian model
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian (via Librarian.objects.get): {librarian}")
    except Library.DoesNotExist:
        print("Library not found:", library_name)
    except Librarian.DoesNotExist:
        print("No librarian found for library:", library_name)

if __name__ == '__main__':
    create_sample_data()
    query_books_by_author('George Orwell')
    list_books_in_library('Central Library')
    get_librarian_for_library('Central Library')
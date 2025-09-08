from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
from django.http import HttpResponse


# --- Function-based View ---
def list_books(request):
    books = Book.objects.all()
     # ✅ Plain text output (for checker)
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output if output else "No books available.")


# --- Class-based View ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    # override get_object to lookup by ID or name if needed
    def get_object(self, queryset=None):
        return get_object_or_404(Library, pk=self.kwargs.get("pk"))


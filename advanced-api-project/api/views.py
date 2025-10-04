from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
#list all books or create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    #Allow unauthenticated GET but restrict create
    def get_permissions(self):
        if self.request.method == 'GET':
            return[permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

# Retrieve, update or delete a specific book
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow unauthenticated GET but restrict update/delete
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]   



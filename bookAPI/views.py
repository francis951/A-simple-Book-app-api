from django.shortcuts import render
from books.models import Book
from .serializers import Bookserializer
from rest_framework import generics

# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
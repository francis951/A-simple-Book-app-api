from rest_framework import serializers
from books.models import Book

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("__all__") 
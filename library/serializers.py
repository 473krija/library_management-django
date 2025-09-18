
from rest_framework import serializers
from .models import Book, Borrower, BorrowRecord, Author
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'genre', 'available_copies']


# Serializer for Borrower model
class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['url', 'id', 'name', 'email', 'joined_date']


# Serializer for BorrowRecord model
class BorrowRecordSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    borrower = serializers.PrimaryKeyRelatedField(queryset=Borrower.objects.all())

    class Meta:
        model = BorrowRecord
        fields = ['url', 'id', 'book', 'borrower', 'borrow_date', 'return_date']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'highlighted']
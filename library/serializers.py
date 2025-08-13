
from rest_framework import serializers
from .models import Book, Borrower, BorrowRecord, Author
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# Serializer for Book model
class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field= 'name')

    class Meta:
        model = Book
        fields = ['url', 'title', 'author', 'published_date', 'genre', 'available_copies']


# Serializer for Borrower model
class BorrowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Borrower
        fields = ['url', 'id', 'name', 'email', 'joined_date']


# Serializer for BorrowRecord model
class BorrowRecordSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')
    borrower = serializers.SlugRelatedField(queryset=Borrower.objects.all(), slug_field='name')

    class Meta:
        model = BorrowRecord
        fields = ['url', 'id', 'book', 'borrower', 'borrow_date', 'return_date']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'highlighted']
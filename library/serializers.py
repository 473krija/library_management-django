
from rest_framework import serializers
from .models import Book, Borrower, BorrowRecord

# Serializer for Book model
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'title', 'author', 'published_date', 'genre', 'available_copies']


# Serializer for Borrower model
class BorrowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Borrower
        fields = ['url', 'id', 'name', 'email', 'phone_number', 'joined_date']


# Serializer for BorrowRecord model
class BorrowRecordSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')
    borrower = serializers.SlugRelatedField(queryset=Borrower.objects.all(), slug_field='name')

    class Meta:
        model = BorrowRecord
        fields = ['url', 'id', 'book', 'borrower', 'borrow_date', 'return_date']

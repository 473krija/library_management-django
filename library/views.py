"""
Views for the library app of the library_management project.
"""

from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404 
from rest_framework import status


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(paginated_books, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------- AUTHORS ----------------------
@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_authors = paginator.paginate_queryset(authors, request)
        serializer = AuthorSerializer(paginated_authors, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'GET':
        serializer = AuthorSerializer(author, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------- BORROWERS ----------------------
@api_view(['GET', 'POST'])
def borrower_list(request):
    if request.method == 'GET':
        borrowers = Borrower.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_borrowers = paginator.paginate_queryset(borrowers, request)
        serializer = BorrowerSerializer(paginated_borrowers, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = BorrowerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def borrower_detail(request, pk):
    borrower = get_object_or_404(Borrower, pk=pk)
    if request.method == 'GET':
        serializer = BorrowerSerializer(borrower, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BorrowerSerializer(borrower, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        borrower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------- BORROW RECORDS ----------------------
@api_view(['GET', 'POST'])
def borrowrecord_list(request):
    if request.method == 'GET':
        borrowrecords = BorrowRecord.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_borrowrecords = paginator.paginate_queryset(borrowrecords, request)
        serializer = BorrowRecordSerializer(paginated_borrowrecords, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = BorrowRecordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def borrowrecord_detail(request, pk):
    borrowrecord = get_object_or_404(BorrowRecord, pk=pk)
    if request.method == 'GET':
        serializer = BorrowRecordSerializer(borrowrecord, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BorrowRecordSerializer(borrowrecord, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        borrowrecord.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def snippet_list(request, format = None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This will also run the .save() in your model (highlighting code)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format = None):
    """
    Retrieve, update, or delete a snippet by id.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response({"error": "Snippet not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
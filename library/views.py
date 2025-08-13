"""
Views for the library app of the library_management project.
"""

from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from rest_framework import status
#from django.shortcuts import render
#from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
#from django.urls import reverse_lazy

# ---------------------- BOOKS ----------------------


#class BookListView(ListView):
   # """Logic for view of list of books"""

    #model = Book
    #template_name = 'book_list.html' #template
    #context_object_name = 'books' # name that used to access data in the template

#class BookDetailView(DetailView):
    #"""Logic for view of details of the books"""

   # model = Book
   # template_name = 'book_detail.html'
   # context_object_name = 'book'

#class BookCreateView(CreateView):
   # """Logic for creating new  books"""
   # model = Book
    #fields = ['title', 'author', 'genre', 'published_date', 'available_copies']
    #template_name = 'book_form.html'
    #success_url = reverse_lazy('book-list')

#class BookUpdateView(UpdateView):
    #"""Logic for updating the books"""
   # model = Book
   # fields = ['title', 'author', 'genre', 'published_date', 'available_copies']
   # template_name = 'book_form.html'
   # success_url = reverse_lazy('book-list')

#class BookDeleteView(DeleteView):
   # model = Book
   # template_name = 'book_confirm_delete.html'
   # success_url = reverse_lazy('book-list')

#class AuthorListView(ListView):

   # model = Author
    #template_name = 'author_list.html'
    #context_object_name = 'authors'

#class AuthorDetailView(DetailView):
    #model = Author
    #template_name = 'author_detail.html'
    #context_object_name = 'authors'

#class AuthorCreateView(CreateView):
    #model = Author
    #fields = ['name', 'birth_date', 'biography']
    #template_name = 'author_form.html'
    #success_url = reverse_lazy('author-list')

#class AuthorUpdateView(UpdateView):
    #model = Author
    #fields = ['name', 'birth_date', 'biography']
    #template_name = 'author_form.html'
    #success_url = reverse_lazy('author-list')

#class AuthorDeleteView(DeleteView):
    #model = Author
    #template_name = 'author_confirm_delete.html'
    #success_url = reverse_lazy('author-list')

#class BorrowerListView(ListView):
    #model = Borrower
    #template_name = 'borrower_list.html'
    #context_object_name = 'borrowers'

#class BorrowerDetailView(DetailView):
    #model = Borrower
    #template_name = 'borrower_detail.html'
    #context_object_name = 'borrowers'

#class BorrowerCreateView(CreateView):
    #model = Borrower
    #fields = ['name','email','joined_date']
    #template_name = 'borrower_form.html'
    #success_url = reverse_lazy('borrower-list')

#class BorrowerUpdateView(UpdateView):
    #model = Borrower
    #fields =  ['name','email','joined_date']
    #template_name = 'borrower_form.html'
    #success_url = reverse_lazy('borrower-list')

#class BorrowerDeleteView(DeleteView):
 #   model = Borrower
  #  template_name = 'borrower_confirm_delete.html'
   # success_url = reverse_lazy('borrower-list')

#class BorrowRecordListView(ListView):
 #   model = BorrowRecord
  #  template_name = 'borrowrecord_list.html'
   # context_object_name = 'borrowrecords'

# class BorrowRecordDetailView(DetailView):
#     model = BorrowRecord
#     template_name = 'borrowrecord_detail.html'
#     context_object_name = 'borrowrecords'

# class BorrowRecordCreateView(CreateView):
#     #import pdb;pdb.set_trace();
#     model = BorrowRecord
#     fields = ['book','borrower','borrow_date','return_date']
#     template_name = 'borrowrecord_form.html'
#     success_url = reverse_lazy('borrowrecord-list')

# class BorrowRecordUpdateView(UpdateView):
#     model = BorrowRecord
#     fields = ['book','borrower','borrow_date','return_date']
#     template_name = 'borrowrecord_form.html'
#     success_url = reverse_lazy('borrowrecord-list')

# class BorrowrecordDeleteView(DeleteView):
#      model = BorrowRecord
#      template_name = 'borrowrecord_confirm_delete.html'
#      success_url = reverse_lazy('borrowrecord-list')

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class BorrowerViewSet(viewsets.ModelViewSet):
#     queryset = Borrower.objects.all()
#     serializer_class = BorrowerSerializer

# class BorrowRecordViewSet(viewsets.ModelViewSet):
#     queryset = BorrowRecord.objects.all()
#     serializer_class = BorrowRecordSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)
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
        serializer = AuthorSerializer(authors, many=True, context={'request': request})
        return Response(serializer.data)
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
        serializer = BorrowerSerializer(borrowers, many=True, context={'request': request})
        return Response(serializer.data)
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
        serializer = BorrowRecordSerializer(borrowrecords, many=True, context={'request': request})
        return Response(serializer.data)
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
"""
Views for the library app of the library_management project.
"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *

class BookListView(ListView):
    """Logic for view of list of books"""

    model = Book
    template_name = 'book_list.html' #template
    context_object_name = 'books' # name that used to access data in the template

class BookDetailView(DetailView):
    """Logic for view of details of the books"""

    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    """Logic for creating new  books"""
    model = Book
    fields = ['title', 'author', 'genre', 'published_date', 'available_copies']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    """Logic for updating the books"""
    model = Book
    fields = ['title', 'author', 'genre', 'published_date', 'available_copies']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

class AuthorListView(ListView):

    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'authors'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'birth_date', 'biography']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'birth_date', 'biography']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author-list')

class BorrowerListView(ListView):
    model = Borrower
    template_name = 'borrower_list.html'
    context_object_name = 'borrowers'

class BorrowerDetailView(DetailView):
    model = Borrower
    template_name = 'borrower_detail.html'
    context_object_name = 'borrowers'

class BorrowerCreateView(CreateView):
    model = Borrower
    fields = ['name','email','joined_date']
    template_name = 'borrower_form.html'
    success_url = reverse_lazy('borrower-list')

class BorrowerUpdateView(UpdateView):
    model = Borrower
    fields =  ['name','email','joined_date']
    template_name = 'borrower_form.html'
    success_url = reverse_lazy('borrower-list')

class BorrowerDeleteView(DeleteView):
    model = Borrower
    template_name = 'borrower_confirm_delete.html'
    success_url = reverse_lazy('borrower-list')

class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'borrowrecord_list.html'
    context_object_name = 'borrowrecords'

class BorrowRecordDetailView(DetailView):
    model = BorrowRecord
    template_name = 'borrowrecord_detail.html'
    context_object_name = 'borrowrecords'

class BorrowRecordCreateView(CreateView):
    #import pdb;pdb.set_trace();
    model = BorrowRecord
    fields = ['book','borrower','borrow_date','return_date']
    template_name = 'borrowrecord_form.html'
    success_url = reverse_lazy('borrowrecord-list')

class BorrowRecordUpdateView(UpdateView):
    model = BorrowRecord
    fields = ['book','borrower','borrow_date','return_date']
    template_name = 'borrowrecord_form.html'
    success_url = reverse_lazy('borrowrecord-list')

class BorrowrecordDeleteView(DeleteView):
     model = BorrowRecord
     template_name = 'borrowrecord_confirm_delete.html'
     success_url = reverse_lazy('borrowrecord-list')


"""
Views for the library app of the library_management project.
"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *

class BookListView(ListView):
    """Logic for view of list of books"""

    model = Book
    template_name = 'book_list.html' #template
    context_object_name = 'books' # name that used to access data in the template

class BookDetailView(DetailView):
    """Logic for view of details of the books"""

    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    """Logic for creating new  books"""
    model = Book
    fields = ['title', 'author', 'genre', 'published_date', 'available_copies']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    """Logic for updating the books"""
    model = Book
    fields = ['title', 'author', 'genre', 'published_date', 'available_copies']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

class AuthorListView(ListView):

    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'authors'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'birth_date', 'biography']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'birth_date', 'biography']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author-list')

class BorrowerListView(ListView):
    model = Borrower
    template_name = 'borrower_list.html'
    context_object_name = 'borrowers'

class BorrowerDetailView(DetailView):
    model = Borrower
    template_name = 'borrower_detail.html'
    context_object_name = 'borrowers'

class BorrowerCreateView(CreateView):
    model = Borrower
    fields = ['name','email','joined_date']
    template_name = 'borrower_form.html'
    success_url = reverse_lazy('borrower-list')

class BorrowerUpdateView(UpdateView):
    model = Borrower
    fields =  ['name','email','joined_date']
    template_name = 'borrower_form.html'
    success_url = reverse_lazy('borrower-list')

class BorrowerDeleteView(DeleteView):
    model = Borrower
    template_name = 'borrower_confirm_delete.html'
    success_url = reverse_lazy('borrower-list')

class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'borrowrecord_list.html'
    context_object_name = 'borrowrecords'

class BorrowRecordDetailView(DetailView):
    model = BorrowRecord
    template_name = 'borrowrecord_detail.html'
    context_object_name = 'borrowrecords'

class BorrowRecordCreateView(CreateView):
    #import pdb;pdb.set_trace();
    model = BorrowRecord
    fields = ['book','borrower','borrow_date','return_date']
    template_name = 'borrowrecord_form.html'
    success_url = reverse_lazy('borrowrecord-list')

class BorrowRecordUpdateView(UpdateView):
    model = BorrowRecord
    fields = ['book','borrower','borrow_date','return_date']
    template_name = 'borrowrecord_form.html'
    success_url = reverse_lazy('borrowrecord-list')

class BorrowrecordDeleteView(DeleteView):
     model = BorrowRecord
     template_name = 'borrowrecord_confirm_delete.html'
     success_url = reverse_lazy('borrowrecord-list')



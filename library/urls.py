
from django.urls import path
#from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
#from .views import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('books/', BookListView.as_view(), name='book-list'),
#     path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
#     path('books/add/', BookCreateView.as_view(), name='book-add'),
#     path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
#     path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
#     path('authors/', AuthorListView.as_view(), name= 'author-list'),
#     path('authors/<int:pk>/', AuthorDetailView.as_view(), name= 'author-detail'),
#     path('authors/add/', AuthorCreateView.as_view(), name= 'author-add'),
#     path('authors/<int:pk>/edit/', AuthorUpdateView.as_view(), name= 'author-edit'),
#     path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
#     path('borrowers/', BorrowerListView.as_view(), name='borrower-list'),
#     path('borrowers/<int:pk>/', BorrowerDetailView.as_view(), name= 'borrower-detail'),
#     path('borrowers/add/', BorrowerCreateView.as_view(), name='borrower-add'),
#     path('borrowers/<int:pk>/edit/', BorrowerUpdateView.as_view(), name='borrower-edit'),
#     path('borrowers/<int:pk>/delete/', BorrowerDeleteView.as_view(), name='borrower-delete'),
#     path('borrowrecords/', BorrowRecordListView.as_view(), name= 'borrowrecord-list'),
#     path('borrowrecords/<int:pk>/', BorrowRecordDetailView.as_view(), name= 'borrowrecord-detail'),
#     path('borrowrecords/add/', BorrowRecordCreateView.as_view(), name= 'borrowrecord-add'),
#     path('borrowrecords/<int:pk>/edit/', BorrowRecordUpdateView.as_view(), name= 'borrowrecord-edit'),
#     path('borrowrecords/<int:pk>/delete/', BorrowrecordDeleteView.as_view(), name='borrowrecord-delete'),
#     path('books/', views.book_list, name='books-list'),

# ]

urlpatterns = [
    path('api/books/', views.book_list, name='book-list'),
    path('api/books/<int:pk>/', views.book_detail, name='book-detail'),

    path('api/authors/', views.author_list, name='authors-list'),
    path('api/authors/<int:pk>/', views.author_detail, name='author-detail'),

    path('api/borrowers/', views.borrower_list, name='borrower-list'),
    path('api/borrowers/<int:pk>/', views.borrower_detail, name='borrower-detail'),

    path('api/borrowrecords/', views.borrowrecord_list, name='borrowrecord-list'),
    path('api/borrowrecords/<int:pk>/', views.borrowrecord_detail, name='borrowrecord-detail'),

    path('api/snippets/', views.snippet_list, name = 'snippet-list'),
    path('api/snippets/<int:pk>/', views.snippet_detail, name = 'snippet-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)





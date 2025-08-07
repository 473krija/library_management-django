"""Admin file for the library_management project"""

from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    """Displaying the details of authors model as list"""

    list_display = (
        "name",
        "birth_date",
        "biography",
        
    )

class BookAdmin(admin.ModelAdmin):
   """Displaying the details of book model as list""" 

   list_display = (
       "title",
       "author",
       "published_date",
       "genre",
       "available_copies",
   )

class BorrowerAdmin(admin.ModelAdmin):
    """Displaying the details of borrower model as list"""

    list_display = (
        "name",
        "email",
        "joined_date",
    )

class BorrowRecordAdmin(admin.ModelAdmin):
    """Displaying the details of borrower record model as list"""

    list_display = (
        "book",
        "borrower",
        "borrow_date",
        "return_date",
        
    )
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)


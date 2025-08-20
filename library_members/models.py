from django.db import models
from library.models import *
    
class MemberProfile(models.Model):
    borrower = models.OneToOneField(Borrower, on_delete = models.CASCADE, related_name = 'profile')
    phone_number = models.CharField(max_length = 20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"profile of {self.borrower.name}"
    
class ReadingClub(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    members = models.ManyToManyField(Borrower, related_name = "clubs", blank = True)
    books = models.ManyToManyField(Book, related_name = "clubs", blank = True)

    def __str__(self):
        return self.name
    
class Fine(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    reason = models.CharField(max_length=200)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.borrower.name} - {self.amount} Rs"


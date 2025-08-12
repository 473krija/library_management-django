from django.db import models
""" Models for the project"""

class Author(models.Model):
    """Inserting the objects field required in the model Author"""

    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    biography = models.TextField()

    def __str__(self):
        # Show the author's name and birth year for clarity
        return f"{self.name} ({self.birth_date.year if self.birth_date else 'Unknown'})"

    
class Book(models.Model):
    """Inserting the objects field required in the model Book"""

    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('SF', 'Science Fiction'),
        ('FAN', 'Fantasy'),
        ('MYS', 'Mystery / Thriller'),
        ('ROM', 'Romance'),
        ('HOR', 'Horror'),
        ('HIS', 'Historical'),
        ('BIO', 'Biography'),
        ('SELF', 'Self-Help'),
        ('PHI', 'Philosophy'),
        ('POE', 'Poetry'),
        ('CH', 'Children'),
        ('YA', 'Young Adult'),
        ('COM', 'Comics / Graphic Novels'),
        ('SCI', 'Science & Technology'),
        ('REL', 'Religion / Spirituality'),
        ('TRAV', 'Travel'),
        ('HEA', 'Health & Fitness'),
        ('EDU', 'Education / Academic'),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    published_date = models.DateField(null=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    available_copies = models.IntegerField(default=0)

    def __str__(self):
        # Show book title and author name
        return f"{self.title} by {self.author.name}"

    
class Borrower(models.Model):
    """Inserting the objects field required in the model Borrower"""

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    joined_date = models.DateField(null=True)

    def __str__(self):
        # Display borrower's name and email for easy identification
        return f"{self.name} ({self.email})"

class BorrowRecord(models.Model):
    """Inserting the objects field required in the model BorrowerRecord"""

    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete = models.CASCADE)
    borrow_date = models.DateField(null=True)
    return_date = models.DateField(null=True)

    def __str__(self):
        # Display a readable summary of the borrowing record
        return f"{self.borrower.name} borrowed '{self.book.title}' on {self.borrow_date}"


  
        

      

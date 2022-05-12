from gettext import dpgettext
from django.db import models
from django.core.validators import MinLengthValidator, int_list_validator
from django.db.models import CheckConstraint, Q
from django.forms import CharField
from django.db.models.functions import Length
from accounts.models import OurUser
from django.db.models import F

def subject_validate(value):
    subjects=["maths","science","cs","biology","desgin"]
    if value.lower() in subjects:
        return True
    return False

models.CharField.register_lookup(Length, 'length')


class Book(models.Model):
    ### book details

    title=models.CharField(max_length=60)
    author=models.CharField(max_length=60)
    edition=models.IntegerField(null=True)
    description=models.CharField(max_length=256)
    ISBN=models.CharField(max_length=13, primary_key=True)
    subjects=models.CharField(max_length=60,validators=[subject_validate])

    rating=models.FloatField(null=True)
    books_available=models.CharField(max_length=60)
    book_Image_url=models.URLField(null=True)

    #for adding constraints on sql level
    class Meta:

        constraints = (
            # for checking in the DB
            models.CheckConstraint(
                check=Q(rating__gte=0.0) & Q(rating__lte=5.0),
                name='rating_range')
            ,
            models.CheckConstraint(
                check=Q(ISBN__length__gte=13) & Q(ISBN__length__lte=13),
                name='ISBN_Length_range')
            
            )

class Fine(models.Model):

    user_id = models.ForeignKey(OurUser, on_delete=models.CASCADE,db_column = "user_id")
    amount_due = models.FloatField(max_length=256)
    amount_paid=models.FloatField(max_length=256)
    due_date = models.DateTimeField(null=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, db_column = 'book_id')

    class Meta:
        db_table = 'Fine'
        unique_together = (('user_id', 'book_id'),)
        
    
    #calculate the fine as rs10* days after due day -amount_paid
    

    
class Issued(models.Model):
    user_id = models.ForeignKey(OurUser, on_delete=models.CASCADE,db_column = "user_id")
    due_date = models.DateTimeField(null=True)
    issued_date=models.DateTimeField(null=False)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, db_column = 'book_id')
    class Meta:
        db_table = 'Issued'
        unique_together = (('user_id', 'book_id'),)

        
class complaint(models.Model):
    user_id = models.ForeignKey(OurUser, on_delete=models.CASCADE,db_column = "user_id")
    title = models.CharField(max_length=300)
    description=models.CharField(max_length=600)
    class Meta:
        db_table = 'complaint'



class Event(models.Model):
    start_time = models.CharField(null=True, max_length=100)
    end_time = models.CharField(null=True, max_length=100)
    title = models.CharField(null=False, max_length = 100)
    venue = models.CharField(null = False, max_length = 100)
    date =  models.DateField(null = False)
    description = models.CharField(max_length=300)
    image_url = models.URLField(null=True)
    class Meta:
        db_table = 'event'
    


from django.contrib import admin

# Register your models here.
from .models import Book,Fine
admin.site.register(Book)
admin.site.register(Fine)
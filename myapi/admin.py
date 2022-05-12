from django.contrib import admin

# Register your models here.
from .models import Book,Fine,Issued,complaint, Event
admin.site.register(Book)
admin.site.register(Fine)
admin.site.register(Issued)
admin.site.register(complaint)
admin.site.register(Event)
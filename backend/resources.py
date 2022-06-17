from random import expovariate
from import_export import resources
from .models import Book


class BookReasource(resources.ModelResource):
    class Meta:
        model = Book

# Retrieve Book Instance

## Command:
```python
from bookshelf.models import Book
books = Book.objects.all() #Retrieve all book instances
for book in books:
    print(book)
    
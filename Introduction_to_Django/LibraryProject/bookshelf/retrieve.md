# Retrieve Book Instance

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")  # Retrieve the book instance
print(book)  # Display the book's attributes


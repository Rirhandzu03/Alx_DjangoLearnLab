# Update Book Instance

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")  # Retrieve the book instance
book.title = "Nineteen Eighty-Four"  # Update the title
book.save()  # Save the changes

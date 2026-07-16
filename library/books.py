books_data = {}

def add_book(book_id, title):
    """Registers a new book into the library system."""
    books_data[book_id] = {"title": title, "status": "Available"}
    return "Book added successfully!"

def get_book(book_id):
    """Retrieves a book's information using its ID."""
    return books_data.get(book_id, "Book not found")

def count_books():
    """Returns the total number of books in the library inventory."""
    return len(books_data)
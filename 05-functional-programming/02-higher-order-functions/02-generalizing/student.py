def find(xs, condition):
    for x in xs:
        if condition(x):
            return x
    return None    


# voorbeeld gebruik
# condition
def is_author(book, author):
    return book.author == author

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# list of books en authors
books = [
    Book("Book 1", "Author 1"),
    Book("Book 2", "Author 2"),
    Book("Book 3", "Author 1"),
    Book("Book 4", "Author 3")
]

# Example usage
result = find(books, lambda book: is_author(book, "Author 10"))

if result:
    print(f"The first book by {result.author} is '{result.title}'")
else:
    print(f"No book found")
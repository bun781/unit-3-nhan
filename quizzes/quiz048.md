# Paper Code
<img width="405" alt="image" src="https://github.com/user-attachments/assets/a8edb105-b9e0-4e66-8979-7e924af29370" />

# Code
```.py
class BOOK:
    def __init__(self, title:str, author:str, isbn:str):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display_info(self):
        return f'The title is {self.title}, the author is {self.author}, and the isbn is {self.isbn}'

class LIBRARY:
    def __init__(self):
        self.books = []
    def add_book(self, book:BOOK):
        self.books.append(book)
    def show_books(self):
        out = ''
        for book in self.books:
            out += book.display_info() + '\n'
        return out
```

# Proof of Work
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/d77372a3-6dd5-4107-98f4-e346731246d9" />

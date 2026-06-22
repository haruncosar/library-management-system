class Book:
    def __init__(self, id, title, author, isbn, is_available=1):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book("slow horses", "palle kuling", 2089)
book2 = Book("mobland", "tom hardy", 2025)

books = [book1, book2]
for book in books:
    print(book.title)
    print(book.author)
    print(book.year)


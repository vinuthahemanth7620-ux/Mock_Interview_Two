
class Book:
    library_name = "City Central Library"

    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def borrow_book(self, student_name):
        self.student_name = student_name
        print("Borrowed by:", self.student_name)

    def display_details(self):
        print("Library Name:", self.library_name)
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Borrowed by:", self.student_name)

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

    @staticmethod
    def library_rules():
        print("Books must be returned within 15 days.")

b1 = Book(101, "Python Programming", "hemanth", 700)
b2 = Book(102, "AIML", "Veena", 600)

b1.borrow_book("Vinutha")
b2.borrow_book("Ranjitha")

Book.change_library_name("Swapna Library")

# Creating two more book objects
b3 = Book(103, "C Programming", "James", 400)
b4 = Book(104, "App Development", "Basavaraj", 600)

b3.borrow_book("Prajwal")
b4.borrow_book("Deepika")


# Displaying all book details
for book in [b1, b2, b3, b4]:
    print("\n-----------------------------------")
    book.display_details()

print(" ")
print("*"*30)

Book.library_rules()
print(" ")


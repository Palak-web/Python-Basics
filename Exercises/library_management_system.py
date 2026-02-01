"""write a library class with no of books and books as two instance  variables.
 Write a program to create a library from this library class and show how you can print all books,
 add a book and get the num of books using diff methods.Show that your program doesnot persist the books after the prog is stopped!"""

class Library:
    books = ["Moby-Dick","The Catcher in the Rye","Rich dad Poor dad"]
    no_of_books = 3

    def add_book(self, new_book):
        self.books.append(new_book)
        self.no_of_books += 1 
        print(self.books)

    def count_books(self):
        return len(self.books)
    
    def all_books(self):
        return (self.books)
    
print("NOTE: Books memory mein stored hain.")
print("Program close karne ke baad data save nahi rahega!")

lib = Library()
print(lib.all_books())
lib.add_book("Can we be Strangers again")
total=lib.count_books()
print(total)


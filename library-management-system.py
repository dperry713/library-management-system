import datetime

# Author class
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_biography(self):
        return self.__biography

    def set_biography(self, biography):
        self.__biography = biography

# Book class
class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_borrowed = False
        self.__due_date = None
        self.__borrower = None
    
    def get_title(self):
        return self.__title

    def is_borrowed(self):
        return self.__is_borrowed

    def borrow(self, borrower):
        self.__is_borrowed = True
        self.__borrower = borrower
        self.__due_date = datetime.datetime.now() + datetime.timedelta(days=14)

    def return_book(self):
        self.__is_borrowed = False
        self.__borrower = None
        self.__due_date = None

    def check_due_date(self):
        return self.__due_date

    def is_overdue(self):
        if self.__due_date and datetime.datetime.now() > self.__due_date:
            return True
        return False

# User class
class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []
        self.__reserved_books = []

    def get_name(self):
        return self.__name

    def borrow_book(self, book):
        if book.is_borrowed():
            print(f"Book '{book.get_title()}' is currently unavailable.")
            reserve_choice = input("Would you like to reserve the book? (y/n): ")
            if reserve_choice.lower() == 'y':
                self.__reserved_books.append(book)
                print(f"You have reserved the book '{book.get_title()}'.")
        else:
            book.borrow(self)
            self.__borrowed_books.append(book)
            print(f"You have borrowed '{book.get_title()}'.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            if book.is_overdue():
                days_overdue = (datetime.datetime.now() - book.check_due_date()).days
                fine = days_overdue * 5  # 5 units per day overdue
                print(f"Book is overdue! You owe a fine of {fine} units.")
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"You have returned '{book.get_title()}'.")

# Library class with file handling
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, title, author, isbn):
        book = Book(title, author, 'Fiction', '2020-01-01')  # Simplified
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")
        self.save_books_to_file()

    def add_user(self, name, library_id):
        user = User(name, library_id)
        self.users.append(user)
        print(f"User {name} added.")
        self.save_users_to_file()

    def save_books_to_file(self):
        with open('books.txt', 'w') as f:
            for book in self.books:
                f.write(f"{book.get_title()} by {book.get_author()}\n")

    def save_users_to_file(self):
        with open('users.txt', 'w') as f:
            for user in self.users:
                f.write(f"{user.get_name()}, ID: {user.get_library_id()}\n")

# Main Menu with new features
def main_menu():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Quit")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author, "123-456")  # Simplified ISBN
        elif choice == '2':
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            library.add_user(name, library_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()

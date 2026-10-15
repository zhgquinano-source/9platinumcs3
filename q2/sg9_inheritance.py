class Publication:
    def __init__(self, title, author):
        # Initializes private attributes
        self._title = title
        self._author = author

    # Getter methods for title
    def get_title(self):
        return self._title
    
    # Setter methods for title
    def set_title(self, title):
        self._title = title
    
    # Getter methods for author
    def get_author(self):
        return self._author
    
    # Setter methods for author
    def set_author(self, author):
        self._author = author
    
    # Displays publicazion info        
    def display_info(self):
        print(f"Title : {self._title}")
        print(f"Author : {self._author}")

# Creates a class for the book info
class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        Publication.__init__(self, title, author)
        self._number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self._number_of_pages

    # Setter method for number_of_pages that prevents negative values
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages <= 0:
            print("The number of pages must be positive.")
        else:
            self._number_of_pages = number_of_pages

    def display_info(self):
        Publication.display_info(self)
        print(f"Number of pages: {self._number_of_pages}")

# Creates a class for magazayn info
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        Publication.__init__(self, title, author)
        self._issue_number = 0
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self._issue_number

    # Setter method for issue_number that prevents negative values
    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("The issue number must be positive.")
        else:
            self._issue_number = issue_number

    def display_info(self):
        Publication.display_info(self)
        print(f"Issue number:{self._issue_number}")

# Create an object of the Publication class
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("Python Programming Guide", "Guido van Rossum")

# Create an object of the Book class
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Clean Code", "Robert C. Martin", 464)

# Create an object of the Magazayhn class
mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Time Staff", 150)

# Prints the final publication info
print("Publication Information:")
pub1.display_info()
print()
pub2.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nBook 2 Information:")
book2.display_info()

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())

print("\nMagazine 2 Information:")
mag2.display_info()
print(mag2.get_issue_number())

# MAMAAAAAAA

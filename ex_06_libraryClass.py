class Library:

    def __init__(self):
        self.books = ["Rich Dad Poor Dad", "Ikigai", "Cracking The Coding Interview"]
        self.num_of_books = len(self.books)

    def showAllBooks(self):
        for book in self.books:
            print("The Books are: ", book)

    def addBook(self, bookName):
        self.books.append(bookName)
        # print("The Book Name is: ", self.bo)
        print(len(self.books))

    def matchBookLength(self):
        self.num_of_books = len(self.books)
        if(self.num_of_books == len(self.books)):
            print("Matched!!")
        else:
            print("Something is going wrong on your program...")

lb = Library()
print(lb.books)
print(lb.num_of_books)
lb.showAllBooks()
lb.addBook("Best Coding Practice")
lb.showAllBooks()
print(lb.books)
# print(lb.num_of_books)
lb.matchBookLength()

    

    
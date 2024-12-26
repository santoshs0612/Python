# write a Library class with no_of_books and books as two instances variables . 
# write a program to createa library from this Libarary class and show how you can
#  print all books,add a book and get athe number of books 
# using different methodsshoww that your program dosent persist the books after the pt=rprogram is stopped 



class Library:
    def __init__(self,no_of_books,books):
        self.no_of_books=no_of_books
        self.books = books
    
    # method to add books 
    def printBooks(self):
        print("Books present in the Library ")
        for book in self.books:
            print(book)
    # add books 
    def addBooks(self,bookName):
        self.books.append(bookName)
        self.no_of_books = self.no_of_books+1
    def noOfBooks(self):
        print(f"No of books present in the Library is {self.no_of_books}")



library = Library(1,["Hello World"])

# print(library.printBooks())
library.addBooks("Wild Life")
print(library.printBooks())
print(library.noOfBooks())
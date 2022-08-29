class Library:
    def __init__(self,name,address,phone_number):
        self.name=name
        self.books = []
        self.address= address
        self.phone_number=phone_number
    def book_take (self,book):
        self.books.append(book)
    def  book_returned(self,book):
        self.books.remove(book)
    def display(self):
        print(self.name,self.address,self.phone_number)
        print("Books:")
        print(self.books)
obj=Library("Praju", "karela", "1236")
obj.book_take("python")
obj.book_take("java")
obj.book_take("c")
obj.display()

obj.book_returned("python")
obj.display()

import os
import time

class Book:
    def __init__(self,name,id,quantity) :

        self.name=name
        self.id=id
        self.quantity=quantity

class User:
    def __init__(self,name,id,password) :

        self.name=name
        self.id=id
        self.password=password
        self.borrowBooks=[]
        self.returnBooks=[]



class library:
    def __init__(self,name) :

        self.name=name
        self.user=[]
        self.book=[]

    
    def add_books(self,name,id,quantity):

        book=Book(name,id,quantity)
        self.book.append(book)
        print(f"Book added successfully")
    
    def add_user(self,name,id,password):

        user=User(name,id,password)
        self.user.append(user)
        print(f"user added")
        return user
    
    def borrow_Books(self,user,token):
        for book in self.book:
            if book.name==token:
                if book in user.borrowBooks:
                    print("Already borrowed \n")
                    return
                elif(book.quantity==0):
                    print("No coppy available")
                    return 
                else:
                    user.borrowBooks.append(book)
                    book.quantity-=1
                    print("Borrowed book successfully....")
                    
                    return
        print(f"We don't have the book {token}!\n")
    
    def return_Books(self,user,token):
        for book in self.book:
            if book.name==token:
                if book in user.borrowBooks:
                    user.returnBooks.append(book)
                    book.quantity+=1
                    user.borrowBooks.remove(book)
                    print("Thanks for reading this")
                    return
                else:
                    print("You don't borrow this book")
                    return
            
        print("Enter correct book name")
                 

library=library("bisso")

library.add_books("c++",22,13)
library.add_books("c#",23,14)
library.add_books("java",24,20)
library.add_books("python",25,15)
library.add_books("OOP",26,18)
library.add_books("Software Engineering",27,19)

library.add_user("zunaid",2001,'zunaid123')

admin=library.add_user("admin",2101017,"admin")

os.system('cls')

currentUser=None

while True:
    if currentUser==None:

        os.system('cls')
        print("-----Assalamualykum------")
        print("")

        option=input("Login or Register (L/R)\nForget Password(F)\n")


        if option=="L":
            Id=int(input("Enter id :"))
            Password=input("Enter password :")
            
            match=False

            for user in library.user:
                if user.id==Id and user.password==Password:
                    currentUser=user
                    match=True
                    break
            if match==False:
                print("\nNo User found !")
                input("Press enter to continue")
        
        elif option=='R':
            Name=input("Enter your Name")
            Id=int(input("Enter id :"))
            Password=input("Enter your password")
            
            match=False
            for user in library.user:
                if user.id==Id:
                    print("User exists! ")
                    match=True
                    break
                    


            if match==False:

                user=library.add_user(Name,Id,Password)
                currentUser=user

            elif match==True:
                option=input("Forget password (Y/N)")
                
                if option=="Y":
                    Id=int(input("Enter id :"))
                    
                    for user in library.user:
                        if user.id==Id:

                            print(f"your password is {user.password}")
                            input("Press enter to continue")
                            break
                elif option=="N":
                    continue
        elif option=='F':
            Id=int(input("Enter id :"))
                    
            for user in library.user:
                if user.id==Id:
                    print(f"your password is {user.password}")
                    
            input("Press enter to continue")
        


    else:
        os.system('cls')

        print(f"Welcome back {currentUser.name}")
        
        if  currentUser.name=='admin':
            print("Option:\n")
            print("1:Add book")
            print("2:Add user")
            print("3:Show all books")
            print("4:Logout")

            ch=int(input("Enter option "))
            if ch==1:
                Name=input("Enter book name :")
                Id=int(input("Enter book id :"))
                Quantity=int(input("Enter the quantity :"))
                

                library.add_books(Name,Id,Quantity)
                input("Press enter to continue")
            if ch==2:
                Name=input("Enter your Name :")
                Id=int(input("Enter id :"))
                Password=input("Enter your password :")
                 
                user=library.add_user(Name,Id,Password)
                input("Press enter to continue")

            if ch==3:
                for books in library.book:
                    print(f"Book id {books.id}\tBook name {books.name}\t{books.quantity}")
                input("Press enter to continue")
            if ch==4:
                currentUser=None
        

        else:
            os.system('cls')
            print("Option:\n")
            print("1:Borrow book")
            print("2:Return book")
            print("3:Show Borrowedbooks")
            print("4:Logout")

            ch=int(input("Enter option :"))
            if ch==1:
                Name=input("Enter book name :")
                
                library.borrow_Books(currentUser,Name)
                input("Press enter to continue")
            if ch==2:
                Name=input("Enter book Name :")
                 
                library.return_Books(currentUser,Name)
                input("Press enter to continue")

            if ch==3:
                for book in currentUser.borrowBooks:
                    print(f"{book.id}\t{book.name}")
                input("Press enter to continue")
            if ch==4:
                currentUser=None




            






            
                        

                        





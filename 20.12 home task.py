import re
import random
class Member:
    def __init__(self,mem_id,name,email):
        self.mem_id=mem_id
        self.name=name
        self.email=email

    def verify_email(self):
        ex=r'[a-z0-9._%+-]+@gmail.com$'
        if re.match(ex,email):
            print("Valid email id")
        else:
            print("Invalid email id")

    def verify_number(self):
        Id=r'^LIB\d{4}$'
        if re.match(Id,mem_id):
            print("Valid member id")
        else:
            self.generate_id()

    def generate_id(self):
        self.mem_id="LIB"+str(random.randint(1000,9999))

class Library(Member):
    def __init__(self,mem_id,name,email,book_id,title,author):
        Member.__init__(self,mem_id,name,email)
        self.book_id=book_id
        self.title=title
        self.author=author

    def display(self):
        print("Member id : ",self.mem_id)
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Borrowed Book id : ",self.book_id)
        print("Title : ",self.title)
        print("Author : ",self.author)


mem_id=input("Enter the member id : ")
name=input("Enter the name : ")
email=input("Enter the email : ")
book_id=input("Enter the book id : ")
title=input("Enter the title : ")
author=input("Enter the author : ")

lib=Library(mem_id,name,email,book_id,title,author)
lib.verify_email()
lib.verify_number()
lib.display()



















        
        








        

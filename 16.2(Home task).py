#Question 1

import re 
class User: 
    def __init__(self, username, password): 
        self.__username = username 
        self.__password = password 
    def set_password(self, password): 
        if len(password) < 8: 
            raise ValueError("Invalid Password !\nPassword must be at least 8 characters long") 
        if not re.search("[0-9]", password): 
            raise ValueError("Invalid Password !\nPassword must contain at least one number") 
        if not re.search("[!@#$%^&*]", password): 
            raise ValueError("Invalid Password !\nPassword must contain at least one special character") 
        self.__password = password 
    def check_password(self, input_password): 
        return self.__password == input_password 
word= User("Rakshana","Password1406@") 
print(word.check_password("Password1406@")) 


 #Question 2

class Product: 
    def __init__(self, name, price, stock): 
        self._name = name 
        self._price = price
        self._stock = stock
    def set_price(self, price): 
        if price <= 0: 
            raise ValueError("Invalid Input!\nPrice must be greater than 0") 
        self._price = price 
    def set_stock(self, stock): 
        if not isinstance(stock, int) or stock < 0: 
            raise ValueError("Invalid input!\nStock must be a non-negative integer") 
        self._stock = stock 
    def get_stock(self): 
        return self._stock 
pro= Product("Pencil", 5.00, 150) 
print(pro.get_stock())   
pro.set_stock(75) 
print(pro.get_stock()) 


 #Question 3

class Student: 
    def __init__(self, name, age, marks): 
        self._name = name 
        self._age = age 
        self._marks = marks 
    def set_name(self, name): 
        self._name = name 
    def get_name(self): 
        return self._name 
    def set_age(self, age): 
        if not 5 <= age <= 100: 
            raise ValueError("Age must be between 5 and 100") 
        self._age = age 
    def get_age(self): 
        return self._age 
    def set_marks(self, marks): 
        if not 0 <= marks <= 100: 
            raise ValueError("Marks must be between 0 and 100") 
        self._marks = marks 
    def get_marks(self): 
        return self._marks 
student = Student("Kanish", 15, 89) 
print(student.get_name())   
print(student.get_age())
print(student.get_marks())    

28.11.24                             Tech Home Task

#Question 1

class Person:
    def getname(self):
        self.name=input("Enter the name : ")
    def display(self):
        print("The name of the student : ",self.name)
        
class Student(Person):
     def getID(self):
         self.getname()
         self.id=input("Enter the ID : ")
     def displayInfo(self):
         self.display()
         print("ID : ",self.id)

S=Student()
S.getID()
S.displayInfo()


#Question 2

class Employee:
    def getEmployeeInfo(self):
        self.name=input("Enter the name of the employee : ")
        self.sal=int(input("Enter the salary of the employee : "))
    def display_details(self):
        print("Name : ",self.name,"\nSalary : ",self.sal)

class Manager(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.dept=input("Enter the department : ")
    def display_department(self):
        self.display_details()
        print("Department : ",self.dept)

emp=Manager()
emp.getDetails()
emp.display_department()

        






        
                     

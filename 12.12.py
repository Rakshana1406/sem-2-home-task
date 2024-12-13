class Student:
    def __init__(self,Id,name,grade):
        self.Id=Id
        self.name=name
        self.grade=grade

    def validate_id(self):
        length=len(self.Id)
        if length==7 and self.Id[0:3]=="STU" and self.Id[3:7].isdigit()==True:
            print("Student Id is Valid")
        else:
            print("Student Id is invalid")
                
    def validate_name(self):
        length=len(self.name)
        if length>=2 and all(char.isalpha() or char.isspace() for char in self.name):
            print("Student name is valid")
        else:
            print("Student name is invalid")

    def validate_grade(self):
        if self.grade[0].isdigit==False:
            print("Invalid grade")
        num=int(self.grade.split(' ')[0])    
        if num<1 and num>12:
            print("Stuent grade id invalid")
        else:
            print("Student grade is valid")

    def displayStudentDetails(self):
        print("Student Id : ",self.Id)
        print("Student Name : ",self.name)
        print(f"Student Grade : {self.grade}th GRADE ")

Id=input("Enter the Id : ")        
Name=input("Enter the name : ")
Grade=input("Enter the grade: ")

Stu=Student(Id,Name,Grade)
Stu.validate_id()
Stu.validate_name()
Stu.validate_grade()
Stu.displayStudentDetails()

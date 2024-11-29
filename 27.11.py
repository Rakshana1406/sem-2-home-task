27.11.24                                                 Tech Home Task

# Question 1

class Student: 
    def __init__(self,student_name,roll_number,mark_1,mark_2,mark_3): 
        self.student_name=student_name 
        self.roll_number=roll_number 
        self.mark_1=mark_1 
        self.mark_2=mark_2 
        self.mark_3=mark_3 
    def calculate(self): 
        tot=self.mark_1+self.mark_2+self.mark_3 
        percent=(tot/300)*100 
        return percent
    def grade(self):
        percent=self.calculate()
        if percent>=85: 
            print("Grade S") 
        elif percent >=75: 
            print("Grade A") 
        elif percent >=65: 
            print("Grade B") 
        elif percent >=55: 
            print("Grade C") 
        elif percent >=50: 
            print("Grade D") 
        else: 
            print("Grade F") 
    def show(self): 
        print(f"Student Name:{self.student_name}") 
        print(f"Roll NO:{self.roll_number}") 
        print(f"Marks:{self.mark_1},{self.mark_2},{self.mark_3}") 
student=Student("John",3267,85,89,84) 
student.show() 
student.calculate() 
student.grade() 


# Question 2

class Student: 
    def __init__(self,student_name,age,course,grade): 
        self.student_name =student_name 
        self.age =age 
        self.course =course 
        self.grade =grade 
    def display(self): 
        print("Name:",self.student_name) 
        print("Age:",self.age) 
        print("Course:",self.course) 
        print("Grade:",self.grade) 
    def __del__(self):
        print("All the details of the student are deleted")
student = Student("John", 18, "Computer Science", "A")
print("\nStudent Details:") 
student.display()
del student









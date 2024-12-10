# Question 1

class Camera:  
    def __init__(self,resolution):  
        self.resolution =resolution 
    def displayCameraDetails(self):  
        print("Camera Resolution : ", self.resolution)   
 
class Phone:  
    def __init__(self,ph_no):  
        self.phone_number = ph_no 
    def displayPhoneDetails(self):  
        print("Phone Number : ", self.phone_number) 
 
class SmartPhone(Camera, Phone):  
    def __init__(self,resolution,ph_no,brand,model):  
        Camera.__init__(self,resolution)  
        Phone.__init__(self,ph_no)  
        self.brand = brand
        self.model = model 
    def displayDeviceDetails(self):
        print("\nSmartphone Details : ") 
        self.displayCameraDetails()  
        self.displayPhoneDetails() 
        print("Brand : ", self.brand,"\nModel : ", self.model) 
        
phone = SmartPhone("1080p-HD",9840978410,"VIVO","V2037",) 
phone.displayDeviceDetails()


#Question 2

class Student: 
    def __init__(self, name, roll_no,course): 
        self.name = name
        self.roll_no = roll_no
        self.course = course 
    def display_student_info(self): 
        print("Student Name : ", self.name,"\nRoll No : ",self.roll_no,"\nCourse : ", self.course) 
         
class StudentAthlete(Student): 
    def __init__(self, name,roll_no, course, sport_name): 
        Student.__init__(self,name,roll_no, course)   
        self.sport_name = sport_name 
    def display_athlete_info(self): 
        self.display_student_info()   
        print("Sport : ", self.sport_name)
        
person= StudentAthlete("Kanish",3412,"Computer Science", "Discus Throw") 
person.display_athlete_info() 

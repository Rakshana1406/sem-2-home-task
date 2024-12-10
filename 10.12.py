10.12.24                                         Tech Task

#Question 1

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def Vehicle_info(self):
        print("Make : ",self.make,"\nModel : ",self.model,"\nYear : ",self.year)

class Car(Vehicle):
    def __init__(self,make,model,year,doors,trunk):
        Vehicle.__init__(self,make,model,year)   
        self.doors=doors
        self.trunk=trunk
    def displayCar(self):
        print("No.of Doors : ",self.doors,"\nTrunk Capacity : ",self.trunk)

class Truck(Vehicle):
    def __init__(self,make,model,year,cargo,axles):
        Vehicle.__init__(self,make,model,year)
        self.cargo=cargo
        self.axles=axles
    def displayTruck(self):
        print("Cargo Capacity : ",self.cargo,"\nNo.of Axles : ",self.axles)

class PickupTruck(Car,Truck):
    def __init__(self,make,model,year,doors,trunk,cargo,axles):
        Vehicle.__init__(self,make,model,year)   
        self.doors=doors
        self.trunk=trunk
        self.cargo=cargo
        self.axles=axles
    def displayPickupTruck(self):
        print("Pickup Truck Details : ")
        self.Vehicle_info()
        self.displayCar()
        self.displayTruck()
        
veh=PickupTruck("Volvo","FH16",2024,4,"Cubic Feet","Tons",3)
veh.displayPickupTruck()


#Question 2

class Product:
    def __init__(self,Id,name,price):
        self.Id=Id
        self.name=name
        self.price=price
    def displayProductDetails(self):
        print("Product ID : ",self.Id,"\nName : ",self.name,"\nPrice : $",self.price)

class Electronics(Product):
    def __init__(self,Id,name,price,warranty,brand):
        Product.__init__(self,Id,name,price)
        self.warranty=warranty
        self.brand=brand
    def displayElectronics(self):
        self.displayProductDetails()
        print("Warranty Period : ",self.warranty,"\nBrand : ",self.brand)

class Clothing(Product):
    def __init__(self,Id,name,price,size,material):
        Product.__init__(self,Id,name,price)
        self.size=size
        self.material=material        
    def displayClothing(self):
        self.displayProductDetails()
        print("Size : ",self.size,"\nMaterial : ",self.material)

ele=Electronics("LAP12345","Dell Insppiron 15",35000,"3 Years","Dell")
clo=Clothing("CLO12345","Salwar",1500,"M","Cotton")
ele.displayElectronics()
clo.displayClothing()



        
     












    
    
        
        
    

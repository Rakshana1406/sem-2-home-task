29.11.24                                      Tech Home Task

#Question 1

class Library:
    def __init__(self,bname,bauthor):
        self.bname=bname
        self.author=bauthor
    def displayLibraryDetails(self):
        print("Book Name : ",self.bname,"\nBook Author : ",self.author)

class Members:
    def __init__(self,name,Id):
        self.name=name
        self.Id=Id
    def displayMemberDetails(self):
        print("Member Name : ",self.name,"\nMember Id : ",self.Id)

class LibraryManagement(Library,Members):
    def __init__(self,bname,bauthor,name,Id):
        Library.__init__(self,bname,bauthor)
        Members.__init__(self,name,Id)
    def DisplayDetails(self):
        self.displayLibraryDetails()
        self.displayMemberDetails()

lib=LibraryManagement("The Post Office","Rabindranath Tagore","Rakshana",3412)
lib.DisplayDetails()


#Question 2

class Restaurant:
    def __init__(self,r_name,menu):
        self.r_name=r_name
        self.menu=menu
    def displayRestaurantDetails(self):
        print("Restaurant Name : ",self.r_name,"\nMenu : ",self.menu)

class Delivery:
    def __init__(self,name,ph_no):
        self.name=name
        self.ph_no=ph_no
    def displayDeliveryDetails(self):
        print("Delivery Person Name : ",self.name,"\nPhone Number : ",self.ph_no)

class Order(Restaurant,Delivery):
    def __init__(self,r_name,menu,name,ph_no):
        Restaurant.__init__(self,r_name,menu)
        Delivery.__init__(self,name,ph_no)
    def displayOrderDetails(self):
        self.displayRestaurantDetails()
        self.displayDeliveryDetails()

Ord=Order("Valli Hotel","Idly,Dosai,Poori","Ragu",8531894470)
Ord.displayOrderDetails()




















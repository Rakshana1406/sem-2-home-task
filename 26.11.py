
# Question 1                                        
class BankAccount:
    
    def  __init__(self,holder_name,account_no,balance):
        self.holder_name=holder_name
        self.account_no=account_no
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            print("Amount deposited successfully")
            self.balance+=amount
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if amount<self.balance:
            print("Amount withdrawn successfully")
            self.balance-=amount
        else:
            print("Insufficient amount")

    def check_balance(self):
        print(f"Balance Amount is {self.balance}")

customer=BankAccount("Rakshana",8531894470,10000)
customer.deposit(5000)
customer.withdraw(2000)
customer.check_balance()



# Question 2

class Cosmetics:
    
    def __init__(self,product_name="eye liner",brand="lakme",price=280,category="Makeup"):
        self.product_name=product_name
        self.brand=brand
        self.price=price
        self.category=category

    def show(self):
        print(f"Product Name is {self.product_name}")
        print(f"Brand is {self.brand}")
        print(f"Price is {self.price}")
        print(f"Category is {self.category}")

product=Cosmetics()
product.show()
        
        























            

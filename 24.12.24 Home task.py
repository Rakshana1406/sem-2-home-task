class PriceCalculate: 
    def __init__(self, base_price, discount_percentage=0, tax_percentage=0):  
        self.base_price = base_price 
        self.discount_percentage = discount_percentage 
        self.tax_percentage = tax_percentage 
    def calculate_final_price(self):  
        if self.base_price < 0 or self.discount_percentage < 0 or self.tax_percentage < 0:  
            raise ValueError("Invalid amount.") 
        else: 
            discount_amount = (self.discount_percentage / 100) * self.base_price 
            tax_amount = (self.tax_percentage / 100) * self.base_price 
            total_price = (self.base_price + tax_amount) - discount_amount 
            return total_price
        
base_price = float(input("Enter the base price : ")) 
tax_percentage = float(input("Enter the tax percentage : ")) 
discount_percentage = float(input("Enter the discount percentage : ")) 
        
try:   
    product_calculator = PriceCalculate(base_price, discount_percentage, tax_percentage) 
    final_price = product_calculator.calculate_final_price() 
    print("The final price : " ,final_price) 
except ValueError as v: 
    print(v) 
    

class Calculator:  
    def __init__(self,number1,number2):  
        self.number1 = number1  
        self.number2 = number2 
    def operation(self):  
        if not isinstance(self.number1, int) or not isinstance(self.number2, int):  
            raise ValueError("Both inputs must be integers.")  
        else: 
            if operation_choice > 4 or operation_choice < 1: 
                raise KeyError("Invalid choice.") 
            else: 
                match operation_choice:  
                    case 1:  
                        return self.number1 + self.number2 
                    case 2:  
                        return self.number1 - self.number2   
                    case 3:  
                        return self.number1 * self.number2 
                    case 4:  
                        if self.number2 == 0:  
                            raise ZeroDivisionError("Cannot divide by zero.") 
                        else:  
                            return self.number1 / self.number2

number1 =int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))                         
                        
try:  
    while True:  
        print("Choose an operation: 1,2,3,4") 
        operation_choice = int(input("Enter your choice: "))  
        calculator = Calculator(number1, number2)  
        result = calculator.operation()
        print("The result is:", result)  
except ValueError as v:
    print(v)  
except KeyError as k:
    print(k)  
except ZeroDivisionError as z:
    print(z) 

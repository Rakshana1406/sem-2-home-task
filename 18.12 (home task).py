class Calculator: 
    def calculate(self,a,b=0,c=0):
        for i in (a,b,c):
            if type(i) not in (int,float):
                raise ValueError("It must be an integer and float")
        if a!=0 and b==0 and c==0:  
            return a*a
        elif a!=0 and b!=0 and c==0: 
            return a+b
        elif a!=0 and b!=0 and c!=0: 
            return  a*b*c  

c=Calculator()
try:
    print(c.calculate(5))
    print(c.calculate(5, 6))
    print(c.calculate(5, 6, 7))
    print(c.calculate(5, 6, "Flower"))
except ValueError as a:
    print(a)

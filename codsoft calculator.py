

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def product(a,b):
    return a*b
def division(a,b):
    return a/b

print("Please Select The Operation:-")
print("1.Addition")
print("2.Subtraction")
print("3.Product")  
print("4.Division") 
operation=int(input("Enter Number Coressponding To The Operation You Want To Perform:- "))            
a=int(input("Enter The First Number:- "))
b=int(input("Enter The Second Number:- "))
if operation == 1:
    print(a,"+",b,"=",add(a,b))
elif operation == 2:
    print(a,"-",b,"=",subtract(a,b))
elif operation == 3:
    print(a,"x",b,"=",product(a,b))
else:
    print(a,"/",b,"=",division(a,b))        


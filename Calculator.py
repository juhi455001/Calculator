def ADD(a,b):
    return a+b
def SUB(a,b):
    return a-b
def MULTI(a,b):
    return a*b
def DIVISION(a,b):
    return a/b
num1=float(input("Enter first number:"))
num2=float(input("Enter Second Number:"))
print("1.ADDITIN\n 2. SUBTRACTION\n 3.MULTIPLICATION\n 4.DIVISION")
choice=input("Enter your choice")
match choice:
    case '1':
        print("Addition of two number is:",ADD(num1,num2))
    case '2':
        print("Subtraction of two number is:",SUB(num1,num2))
    case '3':
          print("Multiplication of two number is:",MULTI(num1,num2))
    case '4':
          if num2==0:
              print("Division is not possible!!")
          else:
              print("Division of two number is",DIVISION(num1,num2))   
    case '5':
        print("Thankyou !! Exiting the calculator")  
    case _:
        print("Invalid choice!!")
                           
     
print("\t************** Welcome to Python mini calculator **************")
print("Choose your operations:")
print("Enter 1 for addition" +
       "\nEnter 2 for subtraction" + 
       "\nEnter 3 for multiplication" + 
       "\nEnter 4 for division" + 
       "\nEnter 5 for power" + 
       "\nEnter 6 for modulus")
print("\t\t****************************")
operation = int(input("Enter your choice: "))
a = int(input("Enter first numebr: "))
b = int(input("Enter second numebr: "))
if(operation == 1):
    print("Result:",a+b)
elif(operation == 2):
    print("Result:",a-b)
elif(operation == 3):
    print("Result:",a*b)
elif(operation == 4):
    print("Result:",a/b)
elif(operation == 5):
    print("Result:",a**b)
elif(operation == 6):
    print("Result:",a%b)
else:
    print("Error")
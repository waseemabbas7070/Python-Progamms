# Display Calculator Menu
print("Welcome to the Basic Calculator!")
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

# Get user's choice
choice = input("Enter your choice (1-5): ")
if choice in ['1','2','3','4']:

    # Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    # Perform the chosen operation

if choice == '1':
        result = num1+num2
        print(f"The Result of Addition : {int(result)} ")
elif choice == '2':
        result = num1-num2
        print(f"The Result of Substraction : {int(result)} ")
elif choice == '3':
        result = num1*num2
        print(f'The result of Multiplication : {int(result)} ') 
elif choice == '4':
        if num1 != 0:
         result = num1/num2
         print(f'The result of Division : {result} ')
        else:
         print("Error : Division by Zero is not Allowed ! ") 
        
        
elif choice == '5': 
        print('Exit')
       
else:
        print("Invalid Choise . Please Select the Valid Option")    



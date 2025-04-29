while True:
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

    # If the choice is one of the operations (1 to 4), ask for numbers
    if choice in ['1','2','3','4']:
        # Get two numbers from the user as floats
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    # Perform the operation based on user's choice
    if choice == '1':
        # Addition
        result = num1 + num2
        print(f"The Result of Addition : {int(result)} ")

    elif choice == '2':
        # Subtraction
        result = num1 - num2
        print(f"The Result of Subtraction : {int(result)} ")

    elif choice == '3':
        # Multiplication
        result = num1 * num2
        print(f'The result of Multiplication : {int(result)} ') 

    elif choice == '4':
        # Division with check for zero division
        if num1 != 0:  # ⚠️ Note: This should be checking num2 instead
            result = num1 / num2
            print(f'The result of Division : {result} ')
        else:
            print("Error : Division by Zero is not Allowed ! ") 

    elif choice == '5':
        # Exit condition - break the loop
        print('Exit')
        break

    else:
        # If the user enters an invalid option
        print("Invalid Choice. Please Select the Valid Option")

# list = [1,3,8,9,3,5,6,2]

# mylist = max(list)

# print(f"{mylist} is a lagest numeber in a list ")


# by user input

Numbers = list(map(int,input("Enter number separated by spaces : ").split()))
largest = max(Numbers)

print(f"The largest number in a list is : {largest}")
import random
low = int(input("Enter the lower  bound : "))
high = int(input("Enter the upper  bound : "))

random_number = random.randint(low , high)

print(f"Random number between {low} and {high} : {random_number }")
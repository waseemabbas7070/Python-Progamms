def gcd(a,b):
    while b != 0:
        a,b =b, a % b
    return a
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print(f"the GCD of the {num1} and {num2} is : {gcd(num1,num1)} ")
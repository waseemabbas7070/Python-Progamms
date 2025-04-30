a = int(input("Enter the first number : "))
b  = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    c,b = b,c

print(f"The numbers in ascending order are : {a}, {b}, {c}")


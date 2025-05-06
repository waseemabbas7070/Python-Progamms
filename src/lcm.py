def lcm(x,y):
    greater = max(x,y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

a = int(input("Enter the first  number : "))
b = int(input("Enter the second number : "))

print(f"the LCM of {a} and {b} is : {lcm(a,b)}")
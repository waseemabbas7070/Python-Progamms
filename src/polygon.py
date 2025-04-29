import math

n = int(input("Please enter the number of sides : "))
s = int(input("Please enter the length of side : "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is : {area:.2f}")

import math  # Importing the math module to use mathematical constants and functions

# Get input for radius and height of the cylinder
radius = float(input("Enter the radius of the cylinder: "))  # Asking user to input radius and converting it to float
height = float(input("Enter the height of the cylinder: "))  # Asking user to input height and converting it to float

# Calculate the volume and surface area
volume = math.pi * radius**2 * height  # Formula for volume of cylinder: πr²h
surface = 2 * math.pi * radius**2 + 2 * math.pi * radius * height  # Formula for surface area: 2πr² + 2πrh

# Print the results with two decimal places
print(f"Volume of the cylinder: {volume:.2f}")  # Display the volume
print(f"Surface area of the cylinder: {surface:.2f}")  # Display the surface area

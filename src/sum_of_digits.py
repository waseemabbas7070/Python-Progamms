num = int(input("Enter a number : "))

sum_of_digits = sum(int(digit) for digit in str(num))
print(f"the sum of the digits is : {sum_of_digits}")
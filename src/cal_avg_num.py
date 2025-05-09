numbers = list(map(int,input("Enter a number seprated by spaces : ").split()))
average = sum(numbers) / len(numbers)

print(f"The average of the number is : {average:.2f}")
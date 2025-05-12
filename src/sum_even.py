numbers = list(map(int,input("Enter numbers separated by spaces : ").split()))
even_sum = sum(num for num in numbers if num % 2 == 0 )
print(f"The sum the even number is : {even_sum}")
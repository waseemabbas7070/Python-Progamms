num = int(input("Enter a number : "))

print(f"factor of {num} are : ")

for i in range(1,num+1):
    if num %  i == 0:
        print(i, end= " ")
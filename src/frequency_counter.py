text = input("Enter a string : ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequencies : ")        
for char , count in frequency.items():
    print(f"{char} : {count}")

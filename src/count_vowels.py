text = input("Enter any string : ")
vowels = "aeiouAEIOU"

count = sum(1 for char in text if char in vowels)
vowels_char = [char for char in text if char in vowels]

print(f"The number of vowels in the string is : {count} : These chars are here : {''.join(vowels_char)}")

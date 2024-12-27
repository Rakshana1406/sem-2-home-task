#converting number to roman
num=int(input("Enter the number : "))
roman_num=[(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),(100, "C"), (90, "XC"), (50, "L"), (40, "XL"),(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I") ]
romans=""
for value,symbol in roman_num:
    while num>=value:
        romans+=symbol
        num-=value
print(romans)


#converting roman into number
roman_num = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 
    'C': 100, 'D': 500, 'M': 1000
}

roman = input("Enter the Roman numeral: ").upper()
num = 0
prev_value = 0

for char in reversed(roman):
    current_value = roman_num[char]
    if current_value < prev_value:
        num -= current_value
    else:
        num += current_value
    prev_value = current_value

print(f"The number is: {num}")





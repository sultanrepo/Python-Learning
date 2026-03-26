numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])

print(f"Even numbers are: {even_numbers}")
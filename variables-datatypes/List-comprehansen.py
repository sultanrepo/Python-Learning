numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])

print(f"Even numbers are: {even_numbers}")

#------------------List Comprehension(Square)----------------------
numbers = [1,2,3,4,5,6,7,8,9,10]
squares = [x*x for x in numbers]
print(f"Square of numbers are: {squares}")


numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers are: {even_numbers}")


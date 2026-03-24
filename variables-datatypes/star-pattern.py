# for i in range(5):
#     for j in range(i+1):
#         print("* ", end="")
#     print() #is used to move to the next line after each row of stars is printed
    
for i in range(5):
    print((i+1) * "* ")
    
#reverse star pattern
for i in range(5,0,-1):
    print(i * "* ")
    
# for number in range(101):
#     if number % 2 == 0:
#         print(f"{number} is even number")
#     else:
#         print(f"{number} is odd number")
from loguru import logger
import math

length = 100
breth = 50
width = 50
area = length * width
bhk = 4
print("The area of rectangle is:", area)
print(type(area))
total_area_of_land = length * breth * width
perimeter_of_length = 2 * (length + width)

logger.info(f"The Total area of land {total_area_of_land} and the perimeter of land {perimeter_of_length}")

print(15//6)
print(math.ceil(15/6))

length_of_land = input("Please enter the langth of your land: ")
breth_of_land = input("Please enter the breth of your land: ")
area_of_land = int(length_of_land) * int(breth_of_land)
logger.info(f"Area of Land {area_of_land}")
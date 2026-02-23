from loguru import logger

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
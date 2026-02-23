from loguru import logger

length = 100
width = 50
area = length * width
bhk = 4
print("The area of rectangle is:", area)
print(type(area));
if length > width:
    print("Length is greater than width")
else:
    print("Width is greater than length")
    
print('My home is a ',bhk,' BHK with an area of {} square feet.')

logger.info(f"The area is {area} and the area square {area**2}");
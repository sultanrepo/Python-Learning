from loguru import logger

length = 50
width = 100
area = length * width

if length > width:
    logger.info("Length is greater than width");
elif area > 6000:
    logger.info("Area is greater than 6000");
else:
    logger.info("Width is greater than length and area is less than 6000");    
    
number = int(input("Please enter a number: "))

if(number % 2 == 0):
    logger.info(f"Number {number} is even")
else:
    logger.info(f"Number {number} is odd")
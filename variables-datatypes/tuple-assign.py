from loguru import logger

data = ([5,6],[6,7,8,9],[3])

numbers = []
for items in range(len(data)):
    for i in range(len(data[items])):
        logger.info(data[items][i])
        numbers.append(data[items][i])
        
logger.info(numbers)
new_tuple = tuple(numbers)
logger.info(f"New Tuple: {new_tuple}")
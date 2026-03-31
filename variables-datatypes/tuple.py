from loguru import logger

test_tuple = (1,2,3,4,5,2, "True", "Sultan", True, False, 1.23, 3.14)
logger.info(test_tuple)

print(test_tuple[5:8])

if 23 in test_tuple:
    logger.info(f"23 is present in the tuple")
else:
    logger.info(f"23 is not present in the tuple")
    
print(test_tuple.count(2))
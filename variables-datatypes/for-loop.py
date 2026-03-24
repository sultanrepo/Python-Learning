from loguru import logger

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
for name in names:
    logger.info(f"Hello, {name}")
    
for i in range(len(names)):
    logger.info(f"Hello, index {i+1}: {names[i]}")
    
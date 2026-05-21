from loguru import logger

set_a = {1,2,3}
set_a.add(4)
set_a.add(5)
logger.info(set_a)
set_a.remove(2)
logger.info(set_a)

names = ["Ali", "Sultan", "Ashraf", "Ali", "Khan"]
new_set = set(names)
logger.info(new_set)

user_names = {"Ali", "Sultan", "Ashraf", "Ali", "Khan"}
for name in user_names:
    logger.info(name)
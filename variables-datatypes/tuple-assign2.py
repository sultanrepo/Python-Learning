from loguru import logger

tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)

power_values = []
for i in range(len(tuple1)):
    power_values.append(tuple1[i] ** tuple2[i])
logger.info(tuple(power_values))
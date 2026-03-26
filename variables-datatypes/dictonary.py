from loguru import logger

employee = {
    "name": "Sultan Ashraf",
    "age": 30,
    "designation": "Data Engineer",
    "department": {
        "name": "Data Science",
        "location": "Banglore"
    }
}

# for key in employee:
#     logger.info(f"employee data: {employee[key]}")
    
for key, value in employee.items():
    logger.info(f"{key}: {value}")

# employee["name"]= "Sultan Ali Khan"

# logger.info(f"Employee name is {employee['name']}")
# logger.info(f"Employee age is {employee['age']}")
# logger.info(f"Employee designation is {employee['designation']}")

# employee["salary"] = 2500000.54
# logger.info(f"Employee details after adding salary is {employee}")

# employee.pop("age")
# logger.info(f"Employee details after removing age is {employee}")
# del employee["designation"]
# logger.info(f"Employee details after deleting designation is {employee}")
# logger.info(f"Employee name is {employee.get('gfsd')}")

# logger.info(f"Employee {employee['department']['name']} is located in {employee['department']['location']}")

# logger.info(f"Keys of employess are: {employee.keys()}")
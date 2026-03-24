from loguru import logger

list1 = [101, "Sultan", 2500000.54, True]
print(list1)

labour_name = ["Ramesh","Suresh","Modi","Rahul"]
logger.info(f"Labour name of 0th index is {labour_name[-1]}")

labour_name.append("Gogol")
labour_name.append("Sundar")
logger.info(f"Labour name after appending is {labour_name}")

new_labor_list = ["Jagmohan", "Rampyare","Roni"]
labour_name.extend(new_labor_list);
logger.info(f"Labour name after extending is {labour_name}")

labour_name.insert(1, "Sivaji")
logger.info(f"Labour name after inserting is {labour_name}")

labour_wage = [["Ramesh",800],["Suresh",9000],["Modi",10000],["Rahul",15000]]
logger.info(f"Lobour with wage details is {labour_wage}")
logger.info(f"Labour with wage details of 0th index {labour_wage[0]}")

logger.info(labour_name[1:2])
logger.info(labour_name[2:6])
logger.info(labour_name[1:6:2])

lst = [1,2,3,4,2]
lst.remove(2)
logger.info(f"List after removing 2 is {lst}")
lst.pop(2)
logger.info(f"List after poping 2nd index is {lst}")
lst.sort(reverse=True)
logger.info(f"List after sorting is {lst}")
print(len(lst))

#--------------------POP-----------------------------------
labour_details = ["Khan", "Ansari", "Shaikh", 400,500,600]
wage = labour_details.pop()
if wage > 500 :
    print("Costly labor charge")
else :
    print("Affordable labor charge")
#----------------------------------------------------------

#--------------------Change Value--------------------------
labour_details = ["Khn", "Ansri", "Shikh", 400,500,600]
labour_details[0:3] = ["Khan", "Ansari", "Shaikh"]
logger.info(f"Labour details after changing value is {labour_details}")

#----------------------------------------------------------

#---------------------Split--------------------------------
hash_code = "ABC-1234-XYZ-5678-PQR-9012-LMN-3456-TUV-7890"
hash_code_split = hash_code.split("-")
logger.info(f"Hash code after split is {hash_code_split}") 


#----------------------------------------------------------
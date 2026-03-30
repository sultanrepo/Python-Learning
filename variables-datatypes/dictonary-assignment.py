# Assignment:-

# Total labour cost if total working days was 50
# out of which mahesh was absent for 3 days and jagmohan was absent for  7 days
# find out the total labour cost?

labour_data = {
    "Sultan": 500,
    "Meraj": 400,
    "Mahesh": 300,
    "Jagmohan": 200,
    "Ejaz": 100,
    "Aftab": 500,
    "Mota": 250
}

total_cost = 0
for key in labour_data:
    total_cost = total_cost + labour_data[key]

total_cost_for_50days = total_cost * 50
mahesh_absent = 3
jagmohan_abset = 7
mahesh_absent_cost = labour_data["Mahesh"] * mahesh_absent
jogmohan_absent_cost = labour_data["Jagmohan"] * jagmohan_abset
absent_sum = mahesh_absent_cost + jogmohan_absent_cost
total_cost_with_absent = total_cost_for_50days - absent_sum
print(f"Total labour cost for 50 days is: {total_cost_for_50days}")
print(f"Total labour cost for 50 days with absent is: {total_cost_with_absent}")

#----------------------------------------------------------------------------------

labour_data = {
    "Sultan": 500,
    "Meraj": 400,
    "Mahesh": 300,
    "Jagmohan": 200,
    "Ejaz": 100,
    "Aftab": 500,
    "Mota": 250
}

# Total daily cost
total_cost = sum(labour_data.values())

# Total for 50 days
total_cost_for_50days = total_cost * 50

# Absent days
mahesh_absent = 3
jagmohan_absent = 7

# Deduct absent cost
mahesh_absent_cost = labour_data["Mahesh"] * mahesh_absent
jagmohan_absent_cost = labour_data["Jagmohan"] * jagmohan_absent

absent_sum = mahesh_absent_cost + jagmohan_absent_cost

# Final cost
total_cost_with_absent = total_cost_for_50days - absent_sum

print(f"Final labour cost: {total_cost_with_absent}")


labour_data = {
    "Sultan": 500,
    "Meraj": 400,
    "Mahesh": 300,
    "Jagmohan": 200,
    "Ejaz": 100,
    "Aftab": 500,
    "Mota": 250
}

print(labour_data.get("Sultan1"))
print(labour_data.keys())
print(labour_data.values())
print(labour_data.items())
labour_data.update({"sultan": 600})
print(labour_data)

new_dict = {
    "Khan": 700,
    "Kamal": 800,
    "Jamal": 900
}

final_dict = {**labour_data, **new_dict}
print(final_dict)
print(f"before pop: {new_dict}")
new_dict.pop("Kamal")
print(f"after pop: {new_dict}")

print(new_dict.popitem())
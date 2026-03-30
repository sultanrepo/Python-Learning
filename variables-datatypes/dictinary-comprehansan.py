labour_data = {
    "Sultan": 500,
    "Meraj": 400,
    "Mahesh": 300,
    "Jagmohan": 200,
    "Ejaz": 100,
    "Aftab": 500,
    "Mota": 250
}

labour_data = {key:labour_data.get(key)+100 for key in labour_data}
print(labour_data)

labour_data = {key:labour_data.get(key)+100 if key != "Sultan" else labour_data.get(key) for key in labour_data}
print(labour_data)

name = "sabreen"
latter_count = {}
for char in name:
    if char in latter_count:
        latter_count[char] +=1
    else:
        latter_count[char] = 1
    print(latter_count)
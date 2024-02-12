
data = [vars(iris) for iris in DATA]
header = data[0].keys()

with open(FILE, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(header))
    writer.writeheader()
    writer.writerows(data)

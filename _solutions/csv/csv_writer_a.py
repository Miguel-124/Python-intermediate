
with open(FILE, mode='w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(DATA)

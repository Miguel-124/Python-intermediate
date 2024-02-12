
result = {}
i = count()

for *_, species in DATA[1:]:
    if species not in result:
        result[species] = next(i)

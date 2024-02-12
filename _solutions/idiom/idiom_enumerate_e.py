
def myenumerate(iterable, start=0):
    current = start
    result = []

    for i in range(len(iterable)):
        row = (current, iterable[i])
        result.append(row)
        current += 1

    return result

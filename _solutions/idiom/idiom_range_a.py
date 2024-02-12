
def myrange(start=0, stop=None, step=1):
    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result

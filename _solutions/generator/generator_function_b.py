
def myrange(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

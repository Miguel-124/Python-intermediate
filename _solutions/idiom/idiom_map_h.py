
def parse(line: str) -> tuple:
    *values, species = line.strip().split(',')
    values = map(float, values)
    return tuple(values) + (species,)

result = map(parse, DATA.splitlines())

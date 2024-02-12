
result = DATA.splitlines()
result = filter(valid, result)
result = map(parse, result)

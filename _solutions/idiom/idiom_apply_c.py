
result = DATA.splitlines()
result = map(str.strip, result)
result = filter(valid, result)
result = map(parse, result)

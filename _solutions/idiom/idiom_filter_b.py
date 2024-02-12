
def valid(line: str) -> bool:
    if len(line) == 0:
        return False
    if line.startswith('#'):
        return False
    return True


result = filter(valid, DATA.splitlines())

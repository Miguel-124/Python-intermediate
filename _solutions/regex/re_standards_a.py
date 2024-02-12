
def is_pesel_valid(pesel):
    if re.match(PATTERN, pesel):
        return True
    else:
        return False


def is_pesel_woman(pesel):
    pesel = str(pesel)
    gender_digit = int(pesel[-2])
    return gender_digit in WOMAN

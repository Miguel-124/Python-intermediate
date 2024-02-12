"""
* Assignment: RE Standards PESEL
* Complexity: medium
* Lines of code: 0 lines
* Time: 5 min
* Warning: Discussion only - do not write any code

English:
    1. Discussion only - do not write any code
    2. Consider Pesel only for people born before year 2000
    3. Having PESEL "69072101234":
       a. What pattern can be at the first place in PESEL?
       a. What pattern can be at the second place in PESEL?
       a. What pattern can be at the third place in PESEL?
       a. What pattern can be at the fourth place in PESEL?
       a. What pattern can be at the fifth place in PESEL?
       a. What pattern can be at the sixth place in PESEL?
    4. What is control digit or control sum?

Polish:
    1. Tylko dyskusja - nie pisz żadnego kodu
    2. Zajmujemy się tylko peselami ludzi urodzonymi przed 2000 rokiem
    3. Mając PESEL "69072101234":
       a. Jakie wyrażenie może być na pierwszym miejscu w PESEL?
       b. Jakie wyrażenie może być na drugim miejscu w PESEL?
       c. Jakie wyrażenie może być na trzecim miejscu w PESEL?
       d. Jakie wyrażenie może być na czwartym miejscu w PESEL?
       e. Jakie wyrażenie może być na piątym miejscu w PESEL?
       f. Jakie wyrażenie może być na szóstym miejscu w PESEL?
    4. Co to jest cyfra kontrolna lub suma kontrolna?
"""
# a. Na pierwszym miejscu w PESEL znajduje się numer roku urodzenia.
# W przypadku "69072101234" oznacza to, że osoba urodziła się w 1969 roku.
# b. Drugie miejsce w PESEL oznacza dwie ostatnie cyfry roku urodzenia.
# W przypadku "69072101234" jest to "69".
# c. Trzecie miejsce w PESEL oznacza numer miesiąca urodzenia.
# W przypadku "69072101234" jest to "07" (lipiec).
# d. Czwarte miejsce w PESEL oznacza dziesiątkę dni miesiąca urodzenia.
# W przypadku "69072101234" jest to "2", ponieważ osoba urodziła się w drugiej dekadzie lipca.
# e. Piąte miejsce w PESEL oznacza jedności dni miesiąca urodzenia.
# W przypadku "69072101234" jest to "1", ponieważ osoba urodziła się pierwszego dnia lipca.
# f. Szóste miejsce w PESEL oznacza płeć.
# Dla osób urodzonych przed 2000 rokiem, liczba parzysta oznacza kobietę,
# a nieparzysta mężczyznę.
# W przypadku "69072101234" ostatnia cyfra to "4", co oznacza, że osoba jest mężczyzną.
#
# 4. Cyfra kontrolna lub suma kontrolna:
# Ostatnia cyfra w numerze PESEL to cyfra kontrolna, która służy do weryfikacji poprawności numeru.
# Jest obliczana na podstawie pozostałych cyfr numeru PESEL i używana do wykrywania błędów
# przy wprowadzaniu numeru lub fałszowania dokumentów.
# W przypadku PESEL "69072101234" cyfra kontrolna to "4", która jest wyliczana na
# podstawie pozostałych cyfr numeru PESEL i spełnia określone reguły matematyczne.


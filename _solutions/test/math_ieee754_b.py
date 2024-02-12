"""
* Assignment: Math IEEE754 IntFix
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:

    2. Run doctests - all must succeed

Polish:
    1. Dane są ceny:
        a. cukierek (candy) = 0,10 USD
        b. ciasteczko (cookie) = 0,20 USD
    2. Zdefiniuj `result: float` z sumą cen za ciasteczko i cukierek
    3. Uwzględnij poprawkę na błąd precyzji wynikający z IEEE-754
    4. W tym celu wykorzystaj typ `int`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result
    0.3
"""

CENT = 1
DOLLAR = 100*CENT

# Total price for both a candy and a cookie
# Use `int` mathematics
# type: int
result = ...

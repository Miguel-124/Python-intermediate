"""
* Assignment: Math IEEE754 DecimalFix
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define `result: Decimal` with result of adding `CANDY` and `COOKIE`
    2. Run doctests - all must succeed

Polish:
    1. Dane są ceny:
        a. cukierek (candy) = 0,10 USD
        b. ciasteczko (cookie) = 0,20 USD
    2. Zdefiniuj `result: Decimal` z sumą cen za ciasteczko i cukierek
    3. Uwzględnij poprawkę na błąd precyzji wynikający z IEEE-754
    4. W tym celu wykorzystaj typ `Decimal`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result
    Decimal('0.30')
"""

from decimal import Decimal


# Total price for both a candy and a cookie
# Use `Decimal` mathematics
# type: Decimal
result = ...

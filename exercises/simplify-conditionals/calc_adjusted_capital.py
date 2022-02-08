# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace nested conditional with guard clauses.

ADJ_FACTOR = 0.7

def elegible_adjusted_capital(capital, rate, duration):
    return capital > 0 and rate > 0 and duration > 0

def calculate_adjusted_capital(duration, income):
    return (income / duration) * ADJ_FACTOR

def get_adjusted_capital(capital, rate, duration, income):
    if elegible_adjusted_capital(capital, rate, duration):
        return calculate_adjusted_capital(duration, income)

adjusted_capital = get_adjusted_capital(50000, 4, 10, 10000)
print(adjusted_capital)

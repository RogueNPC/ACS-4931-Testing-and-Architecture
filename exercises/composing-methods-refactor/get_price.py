# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.
def get_price():
    return get_base_price() * get_discount_factor()

def get_base_price():
    # temp variables
    quantity = 1
    item_price = 9.99
    return quantity * item_price

def get_discount_factor():
    discount_factor = 0
    if get_base_price() > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return discount_factor
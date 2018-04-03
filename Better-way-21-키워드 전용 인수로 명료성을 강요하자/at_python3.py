# -*- coding: utf-8 -*-

def safe_division_c(number, divisor, *,
    ignore_overflow=False,
    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


# safe_division_c(1, 10**500, True, False)

safe_division_c(1, 0, ignore_zero_division=True)

try:
    safe_division_c(1, 0)
except ZeroDivisionError:
    pass


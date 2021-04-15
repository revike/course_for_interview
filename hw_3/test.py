try:
    0/0
except ZeroDivisionError as exc:
    print(exc.__doc__)
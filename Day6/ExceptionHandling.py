import sys
a = [12,45]
try:
    print(a[5])

except IndexError as e:
    print(sys.exc_info())




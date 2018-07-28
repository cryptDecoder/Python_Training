try:
    print(5/0)
except ZeroDivisionError as e:
    print(e)


a = []
try:
    print(a[5])
    print(6/0)
except IndexError as e:
    print(e)
except NameError as e:
    print(e)
except Exception as e:
    print(e)




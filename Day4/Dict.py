# Dictionary


a = {
    'name' : 'Pruthvi',
    'age' : 24,
    'salary' : 120000
}
print(a)
print(id(a))
print(type(a))
print(a['age'])

#update values

a['age'] = 21
print(a)

# clear

a.clear()
print(a)

a.update({'empid':34})
print(a)

#len
len(a)

a.update({'empid':'empname'})
print(a)


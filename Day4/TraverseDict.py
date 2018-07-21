#for loop in dict
#iteration of dict

a = {
    'name' : 'pruthvi','age' : 21,'salary' : 2366
}
for key,value in a.items():
    print(key,value)

#values method
print(a.values())

#get method

print(a.get('name'))
print(a.keys())
i = 0
print(i in a)


print('name' in a.keys())





print(id(a))
a.update({'name':'ab'})
print(id(a))
print(a)

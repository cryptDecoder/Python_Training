#indexing of list
a = [1,5,3,6,7,9,8,2,0,4]
print(a[0])
print(a[-5])
print(a[-9])
print(a[-10])


# function of list

#1: append
a.append(12)
print(a)

#2:len
print(len(a))

#delete
del(a[1])
print(a)

#concate
a+=[12,23,45,65]
print(a)

#remove

a.remove(65)
a.append([0,0,8])
print(a)


# max and min value

b = [20,23,36,45,69,5]
print(max(b))
print(min(b))
print(a[-1])
del(a[-1])
print(a)

a.append([12,36,36,45])
print(a)

print(a[-1])
print(a[-1][0])

#index
c = [10,23,25]
print(c.index(10))
print(c.index(25))

del c[c.index(23)]
print(c)

d=[5,6,4,7]
c.extend(d)
print(c)

n = ["pruthvi"]
print(id(n))
n*=4
print(n)
print(id(n))


#remove

n.remove("pruthvi")
print(n)

#sort

gn = [12,25,36,4]
gn.sort()
print(gn)


#reverse
gn.reverse()
print(gn)


#Replace
gn[0]= 14
print(gn)
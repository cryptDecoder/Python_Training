'''input output operations on file'''


fd = open('D:\Python Training\Day5\Data.txt','w+')
#print(fd.read())

# readline

print(fd.readline())


#readlines

#print(fd.readlines())

#line

for line in fd.readlines():
    print(line)

# mode
print(fd.mode)

print(fd)

print(fd.tell()) #current possition of cursor

print()

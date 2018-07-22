fd = open('D:\Python Training\Day5\Data.txt','w+')


print(fd.mode)
fd.write("Hello python")
print(fd.read())



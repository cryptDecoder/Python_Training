item  = []

no = int(input("\n Enter the number of elements :"))

for i in range(no):
    i = int(input("\n Enter the values :"))
    item.append(i)
print("\n List Before element delete :",item)

ele = int(input("\n Enter the the element which you want to delete :"))
for i in item:
    if(i == ele):
        del item[item.index(ele)]
        print("\n Item deleted successfully..!!")

print("\n List after delete the element",item)

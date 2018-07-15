


items = []
temp = 0
no = int(input("\n Enter the number of elements :"))

for i in range(no):
    item = int(input("\n Enter the Elements :"))
    items.append(item)

print("\n Elements before sort :",items)

for i in range(0,no,1):
    for j in range(0,no,1):

        if items[i] < items[j]:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp


print("\n Elements in ascending order :",items)

for i in range(0,no,1):
    for j in range(0,no,1):
        if items[i] > items[j]:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp

print("\n Elements in descending order :",items)
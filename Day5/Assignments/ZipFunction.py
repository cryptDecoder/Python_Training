

'''
for ind,val in enumerate(sub):
    for ind2,val2 in enumerate(marks):
        if ind == ind2:
            print(val,val2)

'''



new_List = []

def return_min_len():
    if l1>l2:
        return l2

    elif l1<l2:
        return l1
    

sub = ['C programming','data Structure','Java Programming','Cyber Security','python']
marks = [76,78,89,67,96,85]

l1 = len(sub)
l2 = len(marks)

print (return_min_len())
for i in range(return_min_len()):
    new_List.append((sub[i],marks[i]))


print(new_List)





# fo r i in range(len(sub)):
#     if l1 < l2 :
#         new_List.append((sub[i],marks[i]))
#     elif l1 > l2:
#         new_List.append((sub[i],marks[i]))
#
#
#
#
# print(new_List)
#

sub = ['C programming','data Structure','Java Programming','Cyber Security']
marks = [76,78,89,67]

for ind,val in enumerate(sub):
    for ind2,val2 ,in enumerate(marks):
        if ind == ind2:
            print(val,val2)



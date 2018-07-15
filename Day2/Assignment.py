'''Get student name and age and make seating arangment accoding to age '''

name = []
ages = []
no = int(input("\n Enter the nummber of students :"))
for student in range(no):
    student = input("\n Enter the name :")
    name.append(student)
    age = int(input("\n Enter the age :"))
    ages.append(age)

    for age in ages:
        if (age < 18):
            print("\n front seat is allocated to student :")
            print(name)
        elif(age > 18):
            print("\n last seat is allocated to student ...!!!")
            print(name)
"""
    for names in name,age:
        ind = name.index(names)
        indx = ages.index(names)
        print(ind,indx)

    for nd in ind,indx:
        if ind == indx:
            print(name)
"""

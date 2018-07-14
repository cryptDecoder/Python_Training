
#control statements
# if elif else

age = int(input("\n Enter the age :"))

if age == 0:
    print("\n invalid age ...!!!")
elif age < 18:
    print("\n under age person..!!")
elif age > 18 and age < 29:
    print("\n Adult person ..!!")
else:
    print("\n Aged person")


def secondMax():
     ages = [12,36,34,78,77]
     max = 0
     smax =0
     for age in ages:
         if age > max:
             smax=max
             max = age


         elif age < max:
             if smax < age:
                 smax = age
     return smax

second = secondMax()
print(second)                








mat = [3,20,15,20,14,16,1,19,2,10,14,15,6,4,5]
num = len(mat)

numbers = []

for i in range(num):
    for j in range(num):
        if (mat[i] + mat[j] == 20):

            numbers.append(mat[i])
            print("\n First number is :",mat[i]," and Second Number is :",mat[j])

            


print(set(numbers))


def digit_sum(x):
    total = 0
    for i in x:
        try:
            if type(int(i)) == int:
                #print(type(i))

                #print(type(a))
                total += int(i)

            print(total)

        except Exception as e:
            #print(e)
            pass

s = 'ab12cd34ER56'
digit_sum(s)
# def student_data(arg1,arg2,*args):
#     print(arg1,arg2)
#     for arg in args:
#        print(arg)
#
#
#
# student_data('hello','how','r','you','i','am','fine')


def foo(*argv,**krgv):
    print(argv,krgv)



foo(1,2,3,4,name = "Hell",marks = [13,45,6,7,8])

from re import I


def print_numbers():
    for i in range (151):
        print(i)
print_numbers()

def print_numbers_2():
    for i in range (0,1001,5):
        print(i)
print_numbers_2()

def print_numbers_3():
    for i in range (1,100):
        if i %5 == 0 and  i %10 == 0:
            print('coding dojo')
        elif i %5 == 0:
            print('coding')
        else: print(i)
print_numbers_3()

def print_numbers_4():
    sum = 0
    for i in range (1,5000,2):
        sum = sum + i
    print(sum)
print_numbers_4()

def print_numbers_4():
    for i in range (2018,-1,-4):
        print(i)
print_numbers_4()
lowNum = 2
highNum = 9
mult = 3
def print_numbers_5():
    for i in range ({lowNum},{highNum},{mult}):
        print(i)
print_numbers_5()
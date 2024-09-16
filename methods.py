def painter():
    print("Painting")


#painter()


def add():
    a = int(input("Provide number 1: "))
    b = int(input("Provide number 2: "))
    print("Sum is:",a+b)

#add()

def even_or_odd(i):
    if i%2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


#even_or_odd(8)


def pass_or_fail(marks):
    if marks > 35:
        print("Pass")
    else:
        print("Fail")

#a = int(input("Enter your score: "))
#pass_or_fail(a)


def print_range(start, end):
    for i in range(start, end):
        print(i)

#a = int(input("Enter number 1: "))
#b = int(input("Enter number 2: "))
#print_range(a, b)


def painter():
    return "Paint my house"


a = painter()
print(a)

#for i in "apple":
#    print(i)

for i in range(1, 10, 3):
    print(i)


for i in range(11):
    print("2 *", i, "=",2*i)

#a = int(input("Enter number one: "))
#b = int(input("Enter number two: "))

a = 0
b = 0

for i in range(a+1, b):
    print(i)

print("\nNew program\n")

for i in range(1, 10):
    if i%2 == 0:
        print(i)

print("\nNew program\n")

j = 0
for i in range(1, 10):
    if i%2 == 0:
        j = j + 1
print(j)


print("\nNew program\n")

even_number = 0
odd_number = 0

for i in range(1, 10):
    if i%2 == 0:
        even_number = even_number + 1
    else:
        odd_number = odd_number + 1

print("Number of even numbers: ", even_number)
print("Number of odd numbers: ", odd_number)

print("\nNew program\n")
count = 0
for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        count = count + 1
print(count)


print("\nNew program\n")
#input_no = int(input("Enter a number: "))
input_no = 0
for i in range(1, input_no + 1):
    print("The number is", i, "And the cube of the number is",pow(i, 3))

print("\nNew program\n")
for i in range(1, 8):
    print("Week:", i)
    for j in range(1, 8):
        print("Day:", j)

print("\nNew program\n")
for i in range(1, 6):
    result = "*" * i
    print(result)

print("\nNew program\n")
for i in range(1, 5):
    print()
    for j in range(1,i+1):
        print(j, end = "")

print("\nNew program\n")
for i in range(1, 5):
    print()
    for j in range(1, i+1):
        print("*", end = "")

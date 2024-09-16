print("\nNew Program\n")

my_list = []
for i in range(1, 11):
    print("Enter number", i)
    number = int(input())
    my_list.append(number)

sum = 0
for i in my_list:
    sum = sum + i

print(sum)
print(sum/10)

print("Hello World")


"""
a = 'shivbalaji'
b = a.upper()

print(a[4:])

mylist = ["Ram", 45, 65, "Sam", "Shiv", 52.36]

print(mylist[1:3])

mytuple = (45, 87, 96, "Ram")
print(mytuple[-1])

print(len(mylist))


mylist = ["Ram", 45, 65, "Sam", "Shiv", 52.36]
print(mylist[::-1])
b = []
for i in range(1, len(mylist) + 1):
    b.append(mylist[-i])
print(b)

mydict = {"Name": "Ram", "Age": 32}
print(mydict)

del mydict["Age"]

print(mydict)



myfile = open("fruits.csv", "r")
for lines in myfile:
    print(lines, ": Length -", len(lines))
myfile.close()

a = [45, 65, 25, 35]
print("before:",a)

for i in range(len(a)):
    min_element = i
    for j in range(i+1, len(a)):
        if a[min_element] > a[j]:
            min_element = j
        a[i],a[min_element]=a[min_element],a[i]

print("after:",a)

mylist = ["Ram", 1, "Ram", 2]

r = []
for i in mylist:
    if i not in r:
        r.append(i)

print(r)



my_string = "My name is Shiv Balaji"
a = my_string.split()
print(a)
b = " ".join(a)
print(b)


mystring = "mymymynanana"
a = set(mystring)
print(a)

r = []
for i in mystring:
    if i not in r:
        r.append(i)
print(r)

r = []
mylist = [45, 55, 23, 12]

for i in range(1,len(mylist)+1):
    r.append(mylist[-i])

print(r)


fruits = ['apple', 'orange']
new_fruits = ['banana', 'grape']
fruits.extend(new_fruits)
print(fruits)

fruits.pop()

print(fruits)

fruits.insert(3, 45)

print(fruits)

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

print(my_dict['name'])
my_dict['Gender'] = 'Male'
print(my_dict)
my_dict['Gender'] = 'M'
print(my_dict)

del my_dict['Gender']
print(my_dict)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}

print(merged_dict)

dict_one = {n:n**2 for n in range(1, 6) if n%2 != 0}
print(dict_one)


my_dict = {'b': 3, 'a': 1, 'c': 2}
b = {k:my_dict[k] for k in sorted(my_dict)}

v = b.get('d', 'Key not found')
print(v)


my_set = {5, 9, 10, "Ram"}
print(my_set)

my_set.add("Sam")
print(my_set)

my_set.remove("Sam")
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

final_set = set1.union(set2)
print(final_set)

for i in final_set:
    print(i)



final_set = set1.intersection(set2)
print(final_set)

for i in final_set:
    print(i)


my_set = {i**2 for i in range(1,11) if i%2 == 0}
print(my_set)

my_set = {1, 2, 3}
my_frozen_set = frozenset(my_set)

my_set.remove(3)
print(my_set)
print(my_frozen_set)





set3 = set1.difference(set2)
print(set3)


my_list = [1, 5, 23, 23, 6, 5, 1]
my_set = set(my_list)

print(my_set)

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

is_subset = set1.issubset(set2)
print(is_subset)

is_superset = set2.issuperset(set1)
print(is_superset)


coordinates = (10, 20, 30)
x, y, z = coordinates
print(x)
print(y)
print(z)

mylist = [1, 2, 3]
print("\n", mylist[1])

mylist[1] = 100

print(mylist)


my_tuple = (1, 2, 3, 4, 5)
a, b, *c = my_tuple
print(a)
print(b)
print(c)

my_list = [1, 2, 3, 4, 5]

x, y, *z = my_list

print(x, y, z)

my_list = [i**2 for i in range(1, 6)]
print(my_list)

my_list = [i for i in range(0, 11) if i%2 == 0]
print(my_list)

my_list = [i**2 if i%2 == 0 else i**3 for i in range(1, 11)]
print(my_list)

my_list = [i for i in range(1, 20) if i%3 == 0]
print(my_list)

my_list = [i if i%3 == 0 for i in range(1, 20)]
print(my_list)


matrix = [[i for i in range(1, 4)] for _ in range(3)]
print(matrix)

flattened_list = [element for row in matrix for element in row]
print(flattened_list)


my_sentence = "Python is a programming language"
print(my_sentence.split())
mylist = [len(i) for i in my_sentence.split()]
print(mylist)


my_list = [i**2 for i in range(10) if i**2>10]
print(my_list)

a = [1, 2, 3]
b = [4, 5, 6]
c = []
for i in range(len(a)):
    for j in range(len(b)):
        if i == j:
            c.append(a[i] + b[j])
    if i > len(b) - 1:
            c.append(a[i])
        

print(c)

#d = list(zip(a, b))

d = [i+j for i, j in zip(a, b)]
print(d)


a = [1, 2, 3]
b = [4, 5, 6]
c = []
for i in {1, 2, 3}:
    for j in {1, 2, 3}:
        if (i + j) % 2 != 0:
            c.append((i,j))
print(c)


my_set = [1, 2, 3]
c = []
for i in range(len(my_set)):
    for j in range(i+1, len(my_set)):
        if my_set[i] != my_set[j]:
            c.append((my_set[i],my_set[j]))
#print(c)
c = []
for a in range(1, 4):
    for b in range(1, 4):
        if a != b:
            c.append((a, b))
print(c)


my_dict = {i:i**2 for i in range(1, 6)}
print(my_dict)

my_list = ["Python", "is", "beautiful"]

my_dict = {i:len(i) for i in my_list}
print(my_dict)

my_set = {i**2 for i in range(1, 11) if i%2 == 0}
print(my_set)

numbers_list = [1, 2, 3, 4, 5]

print(type(numbers_list))
numbers_iter = iter(numbers_list)
print(type(numbers_iter))
for i in numbers_iter:
    print(i)
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)
print(next(numbers_iter))
print(next(numbers_iter))

numbers_range = range(1, 6)
print(type(numbers_range))
range_iter = iter(numbers_range)
print(type(range_iter))


class squarenumber:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
        #self.result = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.limit:
            result = self.current**2
            self.current += 1
            return result
        else:
            raise StopIteration

a = squarenumber(5)

for i in a:
    print(i)

numbers = [10, 20, 30, 40, 50]
iterator_with_index = enumerate(numbers)

print(iterator_with_index)

for i, j in iterator_with_index:
    print(i, j)

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

a = zip(numbers, letters)

for i in a:
    print(i)

squares_gen_expr = (x ** 2 for x in range(5))

print(type(squares_gen_expr))
for square in squares_gen_expr:
 print(square)


class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        #print('Woof!')
        return 'Woof!'
    
d = dog('Jimmy', 22)
c = d.bark()
print(c)
print(d.bark())

class bank:
    def __init__(self, balance):
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient Balance")

c_one = bank(50000)

c_one.withdraw(10000)



class shape:
    def area(self):
        pass
class circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.14 * (self.radius ** 2)
    
class square:
    def __init__(self, s):
        self.side = s
    
    def area(self):
        return self.side ** 2


c_one = circle(5)
s_one = square(3)

shapes_list = [c_one, s_one]

for i in shapes_list:
    print('Area',i.area())

a = open("fruits.csv", 'r')
b = a.read()
print(b)
a.close()

with open("fruits.csv", 'r') as f:
    g = f.read()
    print (g)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"


point = Point(x=2, y=3)
print(str(point))


age = input("Enter the age: ")



if isinstance(age, int):
    if age>18:
        print('Adult')
    else:
        print('Minor')
else:
    print("Invalid input")



class A:
 def show(self):
  return 'A'

class B:
 def show(self):
  return 'B'

class C(B, A):
 def show(self):
  return super().show()

c_one = C()

print(c_one.show())


class A:
 def show(self):
  return 'A'

class B(A):
 def show(self):
  return super().show() +'B'

class C(A):
 def show(self):
  return  super().show() +'C'

class D(B,C):
 def show(self):
  return super().show() + 'D'

d_one = D()

print(d_one.show())


add = lambda x, y: x + y

print(add(5,5))

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(squared)

for i in squared:
    print(i)

print(type(squared))
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)
print(type(even_numbers))

for i in even_numbers:
    print(i)
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)
print(type(sum_all))

for i in sum_all:
    print(sum_all)


names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]

combined = zip(names, ages)

print(combined)
print(type(combined))

my_list = list(combined)

print(my_list)

score = [95, 12, 36]


all_three = zip(names, ages, score)
my_list_two = list(all_three)
print(my_list_two)
print(my_list_two[0][1])


names = ['Alice', 'Bob', 'Charlie']
age = [25, 30, 22]

for names, age in zip(names, age):
    print(f"{names} is {age} old")

a = ['name', 'age', 'country']
b = ['Alice', 25, 'USA']
user_info = dict(zip(a, b))

print(user_info)


students = [('Alice', 25), ('Bob', 20), ('Charlie', 22)]

a = map(lambda x: x[1], students)

b = list(a)
print(b)


print(sorted(b))



students = [('Alice', 25), ('Bob', 20), ('Charlie', 22)]
students_sorted = sorted(students, key = lambda x: x[1], reverse = True)

print(students_sorted)



def add(*args):
 return sum(args)

result = add(1, 2, 3, 4)

print(result)

def print_info(**kwargs):
 for key, value in kwargs.items():
   print(f"{key}: {value}")

print_info(name="Alice", age=25, country="USA")


#with open('example.csv', 'w') as f:
#    f.write('Hello.\nThis is an example for File handling in Python.\nThank you.')

#with open('example.csv', 'r') as f:
    #read_file = f.readlines()

#for l in read_file:
    #print(l, len(l))

#with open('example.csv', 'a') as f:
    #f.write('\nAppending the following:\nThis is the newly appended line.\nThank you.')


with open('example.csv', 'r') as f:
    mylist = f.readlines()

print(mylist[1])
"""
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 22]}
df = pd.DataFrame(data)


#print(df.head(2))

df['Salary'] = [50000, 60000, 45000]

#print(df)

data = {'Name': ['Alice', 'Bob', 'Charlie'],
 'Age': [25, 30, 22],
 'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)
print(df)

df_one = df.groupby('City')['Age'].mean()

#print(df_one)

city_counts = df['City'].value_counts()

#print(city_counts)

data = {'Name': ['Alice', 'Bob', 'Charlie'],
 'Age': [25, 30, 22],
 'City': ['New York', 'San Francisco', 'Los Angeles']}
df2 = pd.DataFrame({'Name': ['David'], 'Age': [28], 'City': ['Chicago'], 'Salary':
[55000]})

print(data)
print(df2)

concatenated_df = pd.concat([data, df2], ignore_index=True)

#print(concatenated_df)

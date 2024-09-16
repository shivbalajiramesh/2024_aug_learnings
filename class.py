class laptop:
    price = 0
    processor = ""
    ram = ""

hp = laptop()
dell = laptop()
lenova = laptop()

hp.price = 450
dell.price = 750
lenova.price = 500

#print("\n Running Program \n")
#print(hp.price)
#print(dell.price)
#print(lenova.price)



class student:
    def __init__(self):
        self.name = ""
        self.register_no = 0
    def display(self):
        print("Name of the student is:", self.name)
        print("Register number of the student is:", self.register_no)

student_one = student()
student_two = student()

student_one.name = "Ram"
student_two.name = "Sam"
student_one.register_no = 500025
student_two.register_no = 500037

#student_one.display()

class fruit():
    def __init__(self,col):
        self.color = col

    def display(self):
        print("The color of the fruit is:", self.color)

fruit_one = fruit("Red")

#fruit_one.display()


class student:
    def __init__(self, n, reg):
        self.name = n
        self.register_no = reg
    def display(self):
        print("Name of the student is:", self.name)
        print("Register number of the student is:", self.register_no)

student_one = student("Ram", 500025)
student_two = student("Sam", 500037)

#student_one.name = "Ram"
#student_two.name = "Sam"
#student_one.register_no = 500025
#student_two.register_no = 500037

#student_two.display()

class animal:
    def __init__(self, b = "Animal makes sound"):
        self.a = b
    
    def sound(self):
        print(self.a)

class dog(animal):
    pass

#a_one = animal("Dog Barks")
#a_one.sound()

#d_one = dog()
#d_one.a = "Dog Barks"
#d_one.sound()


class person:
    def __init__(self, name = "Default"):
        self.n = name
    
class student(person):
    def __init__(self, grade = 0):
        self.g = grade
    
    def display(self):
        print("Name is:", self.n, "And grade is:", self.g)

#s_one = student(75)
#s_one.n = "Ram"
#s_one.display()

class employee:
    def __init__(self, n = "default", s = 0):
        self.name = n
        self.salary = s

class manager(employee):
    def __init__(self, n, s, d = "default"):
        super().__init__(n, s)
        self.department = d
    
    def display(self):
        print(self.name, self.salary, self.department)

m_one = manager("Ram", 40000, "IT")
m_one.display()
import re
import os

"""
#print(os.getcwd())

os.chdir('C:\\Users\\shivbalaji.ramesh\\OneDrive - CES Limited\\Desktop\\python\\reg_expressions')

#pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
pattern = re.compile(r'[89]00-\d{3}-\d{4}')

with open('data.txt', 'r') as my_file:
    contents = my_file.read()

matches = pattern.finditer(contents)

for i in matches:
    print(i)

"""

s1 = 'bob has a birthday on Feb 25th bob'
s2 = 'sara has a birthday on March 3rd'
s3 = '12eup 586iu'
s4 = '0turt'


#matches = re.search(r'b.{6}y', s1)
matches = re.search(r'b.b', s1)
matches_two = re.finditer(r'b.b', s1)


#print(matches)


for i in matches_two:
    print(i)


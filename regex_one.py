import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

print('Hello World\n')

sentence = 'Start a sentence and bring it to an end.'

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
#pattern = re.compile(r'abc')
#pattern = re.compile(r'\s\d{3}-\d{3}-\d{4}')
#pattern = re.compile(r'[^b]at')
#pattern = re.compile(r'M[rs]+\.\s\w*')
#pattern = re.compile(r'[.\w-]*@[a-zA-z-]*\.[a-zA-z]*')


#pattern = re.compile(r'[a-zA-Z]+\.(com|gov)')

pattern = re.compile(r'http[s]?://w{3}\.')
                     
matches = pattern.finditer(urls)

for i in matches:
    print(i)


pattern_two = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
new_match = pattern_two.finditer(urls)

for i in new_match:
    print(i.group(2) + i.group(3))


substitute = pattern_two.sub(r'\2\3', urls)
print(substitute)

print(urls)
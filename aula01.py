'''
upper()
lower()
len()
replace('str', 'str')
count('str')
find('str')
title()
'''

str = 'ederson schulze'
print(str)
str = str.upper()
print(str)
str = str.lower()
print(str)

str = 'Ederson'
print(len(str))

str = 'edrson'
str = str.replace('edrson', 'Ederson')
print(str)

str = 'ccc bb eeee'
print(str.count('c'))

str= 'Ederson'
print(str.find('E'))

str = 'ederson schulze'

str = str.title()
print(str)
import os
print(os.getcwd())

import csv

# with open('data.csv','r',newline='',encoding='utf-8') as file:
#     x=csv.reader(file)
#     for i in x:
#         print(i)

data = [
    ['name', 'age', 'city'],
    ['Rahul', '25', 'Thane'],
    ['vishal', '2', 'Pune']
]

with open('contact.csv', 'w', newline='', encoding='utf-8') as file:
    x = csv.writer(file)
    x.writerows(data)

# Read and print to check if data is saved correctly
with open('contact.csv', 'r', encoding='utf-8') as file:
    print(file.read())
# create file
# file = open('student.txt','x')   # If file already exists, this line will cause a FileExistsError

# write in file
# file = open('student.txt','w')     #'w' mode overwrites the file 
# file.write('hello all!')
# file.write(' i will not overwrite the previous text. i will add after the previous text')
# file.close()


# read file
# file = open('student.txt','r')
# text = file.read()
# print(text)     # hello all! i will not overwrite the previous text. i will add after the previous text
# file.close()

# append into file 
# file = open('student.txt','a')
# file.write('i have not overwritten the file text')
# file.close()

# w+ is write then one more operation (eg: here write then read)
# file = open('student.txt','w+')
# file.write('hello coders')   # will overwrite
# file.seek(0)  # bcoz if you read after write then the cursor will be at the end of of the text, so seek() will get the cursor back to index 0
# file.seek(2)  # cursor at index 2
# print(file.read())     # llo coders
# file.close()

# a+   append and then one more operation 
# with open('student.txt', 'a+') as file:
#     file.write('Appended text!\n')  # Append text
#     file.seek(0)                    # Move to start of file to read
#     print(file.read()) 

# readline
# file = open('student.txt','r')
# x = file.readline()
# print(x)
# x = file.readline()
# print(x)
# file.close()


# readlines
# file = open('student.txt','r')
# x = file.readlines()
# print(x)   # ['hello codersAppended text!\n', 'hello line 2\n', 'hello 3\n']
# file.close()


# readlines again
# file = open('student.txt','r')
# x = file.readlines()
# for i in x:
#     print(i, end='') 
# file.close()
'''
hello codersAppended text!
hello line 2
hello 3
'''


# to not write file.close() again and again and also not to declare the file again and again
# with open('student.txt','w') as f:    # overwrite
#     f.write('ello world h')


# writelines()   to write   overwrite
# with open('student.txt','w') as f:    
#     x = ['hello\n', 'new\n', 'world\n']
#     f.writelines(x)


# to write in binary form 
# with open('student.txt','wb') as f:
#     x = b'hello stud'
#     f.write(x)



import os
# os.rename('student.txt', 'renamed.txt')    
# os.remove('E:\\coders.txt')
# os.makedirs('Pro new folder')
print(os.getcwd())  # get current working directory    # D:\college DSA training Python
print(os.listdir())  # gives all files in the current working directory
os.chdir('D://')  # change directory
os.mkdir('amit')

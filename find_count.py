s = "python is a programming language"
print(s.find("is"))   # prints strating index of 'is' in s
print(s.find('java')) # prints -1 as 'java' is not present in s

print(s.find('p'))    # prints 10 as 'a' is present in s

print(s.count('p'))  # prints 2 as 'p' is present 2 times 
print(s.count('java')) # prints 0 as 'java' is not present in s
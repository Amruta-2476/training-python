s = 'sandip','ashish','nilesh'
print(type(s))   #  In Python, separating values by commas without using parentheses, brackets, or braces implicitly creates a tuple.
print(' '.join(s))

# .join() to combine the elements of the tuple into a single string
# join() operates on an iterable of strings

m = '|'.join(s)
print(m)
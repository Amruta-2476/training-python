# import example
import example as e        # aliasing a module

# example.add(5,3)    # sum 8
e.add(5,3)    # sum 8
e.sub(5,3)

# to import specific function from module 
from example import specific
specific()


# to import all functions directly   from example import *
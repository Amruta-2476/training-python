# 4 ways to access module:
# 1st way 
'''
import module1
print(module1.pi)
module1.square(4)
module1.welcome('amruta', 'pawar')
module1.login('amruta', 'amruta')
'''

# 2nd way : alias or shortcut name
'''
import module1 as m1
print(m1.pi)
m1.square(4)
m1.welcome('amruta', 'pawar')
m1.login('amruta', 'amruta')
'''

# 3rd way : from module import specific func/var/class/etc
from module1 import square,pi,welcome
square(4)
print(pi)
welcome('amruta', 'pawar')

# 4th way : from module import all
from module1 import *
square(4)
print(pi)
welcome('amruta', 'pawar')


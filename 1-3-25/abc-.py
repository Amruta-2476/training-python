from abc import ABC, abstractmethod     # abstract base classes
# ABC is a class


# abstract class should have atleast ONE abstractmethod

class Bank(ABC):    # ABC is abstract class so it needs to be inherited  
    def loan(self):
        print('1cr loan approved')

    @abstractmethod    # decorator needs to be used
    def provideAadhaar(self):    # this is also do-nothing abstract method, bcoz of @abstractmethod
        pass  # Must be implemented by subclasses
    # hence cannot make class of Bank bcoz of this abstract method
    # TypeError: Can't instantiate abstract class Bank without an implementation for abstract method 'provideAadhaar'



# so create another child class of Bank
class Customer(Bank):
    def provideAadhaar(self):
        print('my aadhaar number is ..x..x')

c1 = Customer()
c1.loan()
c1.provideAadhaar()

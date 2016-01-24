"""
http://www.codewars.com/kata/526dad7f8c0eb5c4640000a4

Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1,2,3])
b = Vector([3,4,5])
c = Vector([5,6,7,8])
a.add(b) # should return Vector([4,6,8])
a.subtract(b) # should return Vector([-2,-2,-2])
a.dot(b) # should return 1*3+2*4+3*5 = 26
a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
a.add(c) # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString function, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals function, so that two vectors who have the same components are equal
The test cases will utilize the user-provided equals method.
"""

#My solution:

class Vector:
  # TODO: Finish the Vector class.
    def __init__(self, vec):
        self.vec = vec       
    
    def add(self,second):           
        if self.length(second):
            return Vector([sum(i) for i in zip(self.vec,second.vec)])
    
    def subtract(self,second):
        if self.length(second):
            return Vector([a-b for a,b in zip(self.vec,second.vec)]) 
    
    def dot(self, second):
        if self.length(second):
            return sum([a*b for a,b in zip(self.vec,second.vec)]) 

    def norm(self):
        return (sum([i**2 for i in self.vec]))**0.5

    def __str__(self):
        temp = str(tuple(self.vec))        
        return temp.replace(" ", "")
        
    def length(self,second):
        if len(self.vec) == len(second.vec):
            return True

        else:
            print ("Vectors are not the same length!")
            return False
            
    def equals(self, second):
        if self.vec == second.vec:
            return True
        else:
            return False

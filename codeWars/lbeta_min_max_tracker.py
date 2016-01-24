"""
http://www.codewars.com/kata/54d512973a742a920d0001be

You've started a heating company with an oddly-mathematical All-Time Max, Min, Mean and Mode Temperature Guarantee™.

Write a class TempTracker with these methods:

insert()    # records a new temperature
get_max()   # returns the highest temp we've seen so far
get_min()   # returns the lowest temp we've seen so far
get_mean()  # returns the mean of all temps we've seen so far
get_mode()  # returns the temp we've seen the most times so far
Do not store every single temperature inserted. You expect to get so much input that you won't be able to store all the temperatures in memory. Optimize for space and time. The time and space costs of your functions should all be O(1)!

The function to get the mean should return a float, but the rest of the get functions can return integers. If no temperatures have been inserted yet, the get functions should return null objects. Temperatures will all be inserted as integers. You'll record your temperatures in Fahrenheit, so you can assume they'll all be in the range 0 to 110.

If there is more than one mode, return any of the modes.
"""

#My solution:

class TempTracker:

    def __init__(self):
        # initialize instance variables
        self.max = None
        self.min = None
        self.mean = None
        self.mode = None
        self.counter = 0
        self.countTemps = [0] * 111

    def insert(self, temperature):
        # insert new temperature
        self.counter += 1
        
        if not self.min or temperature< self.min:
            self.min = temperature
        if not self.max or temperature > self.max:
            self.max = temperature
        
        #if not self.mean:
        if self.mean == None:
            self.mean = 0.0
        self.mean = ((self.mean * (self.counter-1)) + temperature)/self.counter
        
        #if not self.mode:
        self.mode = 0
        self.countTemps[temperature] += 1
        self.max_value = max(self.countTemps)
        self.mode = self.countTemps.index(self.max_value)
  
    def get_max(self):
            return self.max
  
    def get_min(self):
            return self.min
  
    def get_mean(self):
            return self.mean
  
    def get_mode(self):
            return self.mode
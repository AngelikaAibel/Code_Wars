"""
http://www.codewars.com/kata/558ee8415872565824000007

Create a function isDivisible(n,...) that checks if the first agrument n is divisible by all other arguments (return true if no other arguments)
"""

#My solution:

def is_divisible(n,*args):
        
    if len(filter(lambda x: n % x == 0, args)) == len(args):
        return True
    else:
        return False
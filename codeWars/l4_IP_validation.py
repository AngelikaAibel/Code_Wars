"""

http://www.codewars.com/kata/515decfd9dcfc23bb6000006

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. Input to the function is guaranteed to be a single string.

Examples of valid inputs: 1.2.3.4 123.45.67.89

Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089
"""

#My solution:

def is_valid_IP(strng):
    return len(strng.split('.')) == 4 and all(map(lambda x: x[0] != '0' and x.isdigit() and int(x) < 256 ,strng.split('.'))) 
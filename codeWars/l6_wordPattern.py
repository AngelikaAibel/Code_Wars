"""
http://www.codewars.com/kata/word-patterns/python

Write

word_pattern(pattern, string)
that given a pattern and a string str, find if str follows the same sequence as pattern. 

For example:

word_pattern('abab', 'truck car truck car') == True
word_pattern('aaaa', 'dog dog dog dog') == True
word_pattern('abab', 'apple banana banana apple') == False
word_pattern('aaaa', 'cat cat dog cat') == False
"""

#My Solution:
def word_pattern(pattern, string):
    str_arr = string.split(" ")

    dict = {}

    if len(str_arr) != len(pattern):
        return False
        
    if len(list(set(str_arr))) != len(list(set(pattern))):
        return False
        
    else:
        for i, c in enumerate(pattern):
            if not dict.get(c):
                dict[c] = [str_arr[i]]
                
            else:             
                if str_arr[i] != dict[c][0]:
                    return False
                else:
                    pass                

        return True
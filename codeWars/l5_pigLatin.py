"""
http://www.codewars.com/kata/simple-pig-latin/python

Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay



"""

#My Solution:
def pig_it(text):

    temp = text.split(' ')

    result = " ".join([(x[1::]+ x[0] + "ay") if x.isalpha() else x for x in temp])

    print result
    return result
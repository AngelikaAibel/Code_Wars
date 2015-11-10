"""
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.
"""

def rot13(message):
    alph_Upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    new_message = ""
    for m in message:
        
        if m.isalpha():        
            index = alph_Upper.index(m.upper())
            
            if m.isupper():
                if index < 13:
                    new_message += alph_Upper[index + 13]
                else:
                    new_message += alph_Upper[index - 13] 
            else:
                if index < 13:
                    new_message += alph_Upper[index + 13].lower()
                else:
                    new_message += alph_Upper[index - 13].lower() 
                
        else:
            new_message += m
            
    return new_message 

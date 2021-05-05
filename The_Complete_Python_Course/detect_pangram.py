"""
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""
 
        
a_z = "abcdefghijklmnopqrstuvwxyz"

panagram = input(str('please input a panagram : '))

def panagram_phrase(a_z,panagram):
    for letter in a_z: 
        # print(f'these are the letters in the alphabet: ',letter)
        if letter in panagram: 
            print(f'these are the letters in the panagram: ', letter,panagram)
            
        else:
            print('the letters are not in the panagram: ', letter.upper())
            
        
    
panagram_phrase(a_z,panagram)
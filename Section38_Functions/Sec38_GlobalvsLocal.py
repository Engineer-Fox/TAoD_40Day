number = 3

def times_ten(x):
    '''multiply by 10'''
    print('Current value:', str(x))
    x *= 10
    print('Updated Value: ',str(x))
    return x
def char_replace(word):
    '''Replace specific characters in a string with other characters.'''
    while 'a' in word:
        word = word.replace('a','@')
    while 'e' in word:
        word = word.replace('e','3')
    while 'i' in word:
        word = word.replace('i','!')
    while 'o' in word:
        word = word.replace('o','0')
    while 'u' in word:
        word = word.replace('u','#')
    while 'y' in word:
        word = word.replace('y','&')
    print(word)
    # The return is what allows the print(phrase)
    # to work after running the char_replace
    return word

number = 3
times_ten(number)

phrase = input('What phrase would you like to check?: ')
print(phrase)
phrase = char_replace(phrase)
print(phrase)
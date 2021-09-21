def  eliminate_duplicate(chars):
    s = chars
    def change_cases(s):
      return str(s).upper(), str(s).lower()
    result = map(change_cases, chars)
    print(set(result))

 
 

    """ Write a code to convert all the characters in uppercase and lowercase 
    and eliminate duplicate letters from a given sequence. Use map() function. """


chars = {'f', 'b', 'U', 'i', 'o', 'E','a', 'E','a'}
eliminate_duplicate(chars)
# Expected Result: {('U', 'u'), ('O', 'o'), ('A', 'a'), ('B', 'b'), ('F', 'f'), ('I', 'i'), ('E', 'e')}

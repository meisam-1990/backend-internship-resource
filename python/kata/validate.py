def validate(s):
    messg = []
    if not any(x.isupper() for x in s):
        messg.append('String must have 1 upper case character.')
    if not any(x.islower() for x in s):
        messg.append('String must have 1 lower case character.')
    if not any(x.isdigit() for x in s):
        messg.append('String must have 1 number.')
    if len(s) < 8:
        messg.append('String length should be atleast 8.')    
    if not messg:
        messg.append('Valid string.')
    return messg
    """ Write a code to check whether a given string contains a capital letter, 
    a lower case letter, a number and a minimum length. Minimum length must be grader than 5 """


print(validate('D3veloper'))
# Expected Result: ['Valid string']

print(validate('Word'))
# Expected Result: ['Minimum string length must be greater than 5', 'The word must also contain a number']



 
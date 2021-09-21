def print_me(f):
    def inner(*args, **kwargs):
        print(f(*args, **kwargs))
    return inner
     





    #""" Implement decorator to print result of function """
    

@print_me
def add(x, y):
    return x + y

add(10, 20)
# Expected Output: 30

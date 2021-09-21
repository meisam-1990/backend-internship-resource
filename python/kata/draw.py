def draw_triangle(n):
    """ Write a code to construct the following pattern, 
    using a nested for loop. """
    
    for i in range(n):
        for j in range(i):
            print ('* ', end="")
        print('')

    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')






print(draw_triangle(8))
""" Expected Result:

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""

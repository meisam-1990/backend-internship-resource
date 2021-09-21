def just_integer(collection):
    j=[]
    for i in collection:
        if isinstance(i, int):
            j.append(i)
    return j


    """ Write a code to filter collection to get integer values
    using Python filter and local function. """



c = ['Kourosh', 1, None, True, [], 2, 3, ()]


print(just_integer(c))
 
#assert just_integer(c) == [1, 2, 3]


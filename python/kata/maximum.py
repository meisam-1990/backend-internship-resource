from collections import defaultdict

def max_aggregate(score_list):
    """ Write a code to calculate the maximum aggregate from the list of tuples (pairs). """
    temp = defaultdict(int)
    for name, marks in score_list:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])




print(max_aggregate([
    ('Juan Whelan', 90), 
    ('Sabah Colley', 88), 
    ('Peter Nichols', 7), 
    ('Juan Whelan', 122), 
    ('Sabah Colley', 84)
]))

# Expected Result: ('Juan Whelan', 212)

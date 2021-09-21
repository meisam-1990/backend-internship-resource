import datetime
def timestamp_to_date(timestamp):
    """ Write a code to convert timestamp string to readable date. """
    return( datetime.datetime.fromtimestamp( int("1284105682")).strftime('%Y-%m-%d %H:%M:%S'))


print(timestamp_to_date('1630839136'))
# Expected Result: 2021-09-05 15:22:16 

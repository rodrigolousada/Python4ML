def decision(x):
    # >>>>> YOUR CODE HERE
    if x[0] == 'yes':
        if x[1] < 29.5:
            return 'less'
        else:
            return 'more'
    else:
        if x[2] == 'good':
            return 'less'
        else:
            return 'more'
    # <<<<< END YOUR CODE
    

# Test
x = ('yes', 31, 'good')
assert decision(x) == 'more'
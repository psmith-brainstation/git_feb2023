# BrainStation 2023
# 2023-02-28
# Class activity: each student works on a specific ticket
'''
Returns a random string of a specified length

Inputs
----
length  -   the length of the string

'''
# def rand_string_generator(length):
    

#     np.random.choice()

length=1

def rand_string_generator(length):
    if len(length)<1:
        return 'Error: length shorter than required length of ≥1'
    else:
        return 'This is the appropriate length'

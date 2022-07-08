import random

def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''

    return random.randrange(0, 101, 2)

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10



print(genEven())
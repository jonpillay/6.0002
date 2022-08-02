import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    wins = 0
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'B', 'B', 'B']
        hand = []
        for i in range(0,3):
            ball = random.choice(bucket)
            bucket.remove(ball)
            hand.insert(-1, ball)
            if len(hand) >= 1 and hand[i] != hand[i-1]:
                break
            if len(hand) == 3:
                wins += 1
                break
    return float(wins)/float(numTrials)

print(noReplacementSimulation(3000000))
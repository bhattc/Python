hand = {'a': 1, 'c': 2, 'u': 2, 't': 2, 'y': 1, 'h': 1, 'z': 1, 'o': 2}
def calculatehand(hand):
    tothand = 0
    for a in hand:
        tothand += hand[a]
    print tothand
    

# -*- coding: utf-8 -*-

#import random
from math import comb
from itertools import permutations
from itertools import combinations

def ordered_subsets(elements):
    n = len(elements)
    result = []
    for k in range(1,n + 1):          # sizes 1..n
        for p in permutations(elements, k):
            result.append(p)
    return result
    
def k_subsets(elements,k):
    #n = len(elements)
    result = []
    for c in combinations(elements,k):
        result.append(c)
    return result

perm = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
        [1,2,3,0,13,14,15,12,5,6,7,4,17,18,19,16,9,10,11,8,23,20,21,22],
        [2, 3, 0, 1, 18, 19, 16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 22, 23, 20, 21],
        [3, 0, 1, 2, 11, 8, 9, 10, 19, 16, 17, 18, 7, 4, 5, 6, 15, 12, 13, 14, 21, 22, 23, 20],
        [4, 5, 6, 7, 20, 21, 22, 23, 11, 8, 9, 10, 13, 14, 15, 12, 0, 1, 2, 3, 16, 17, 18, 19],
        [5, 6, 7, 4, 14, 15, 12, 13, 21, 22, 23, 20, 1, 2, 3, 0, 8, 9, 10, 11, 19, 16, 17, 18],
        [6, 7, 4, 5, 2, 3, 0, 1, 15, 12, 13, 14, 9, 10, 11, 8, 22, 23, 20, 21, 18, 19, 16, 17],
        [7, 4, 5, 6, 10, 11, 8, 9, 3, 0, 1, 2, 23, 20, 21, 22, 12, 13, 14, 15, 17, 18, 19, 16],
        [8, 9, 10, 11, 5, 6, 7, 4, 22, 23, 20, 21, 0, 1, 2, 3, 19, 16, 17, 18, 14, 15, 12, 13],
        [9, 10, 11, 8, 1, 2, 3, 0, 6, 7, 4, 5, 16, 17, 18, 19, 23, 20, 21, 22, 13, 14, 15, 12],
        [10, 11, 8, 9, 17, 18, 19, 16, 2, 3, 0, 1, 20, 21, 22, 23, 7, 4, 5, 6, 12, 13, 14, 15],
        [11, 8, 9, 10, 21, 22, 23, 20, 18, 19, 16, 17, 4, 5, 6, 7, 3, 0, 1, 2, 15, 12, 13, 14],
        [12, 13, 14, 15, 7, 4, 5, 6, 0, 1, 2, 3, 22, 23, 20, 21, 17, 18, 19, 16, 10, 11, 8, 9],
        [13, 14, 15, 12, 23, 20, 21, 22, 4, 5, 6, 7, 18, 19, 16, 17, 1, 2, 3, 0, 9, 10, 11, 8],
        [14, 15, 12, 13, 19, 16, 17, 18, 20, 21, 22, 23, 2, 3, 0, 1, 5, 6, 7, 4, 8, 9, 10, 11],
        [15, 12, 13, 14, 3, 0, 1, 2, 16, 17, 18, 19, 6, 7, 4, 5, 21, 22, 23, 20, 11, 8, 9, 10],
        [16, 17, 18, 19, 0, 1, 2, 3, 9, 10, 11, 8, 15, 12, 13, 14, 20, 21, 22, 23, 4, 5, 6, 7],
        [17, 18, 19, 16, 12, 13, 14, 15, 1, 2, 3, 0, 21, 22, 23, 20, 10, 11, 8, 9, 7, 4, 5, 6],
        [18, 19, 16, 17, 22, 23, 20, 21, 13, 14, 15, 12, 11, 8, 9, 10, 2, 3, 0, 1, 6, 7, 4, 5],
        [19, 16, 17, 18, 8, 9, 10, 11, 23, 20, 21, 22, 3, 0, 1, 2, 14, 15, 12, 13, 5, 6, 7, 4],
        [20, 21, 22, 23, 16, 17, 18, 19, 10, 11, 8, 9, 14, 15, 12, 13, 4, 5, 6, 7, 0, 1, 2, 3],
        [21, 22, 23, 20, 15, 12, 13, 14, 17, 18, 19, 16, 5, 6, 7, 4, 11, 8, 9, 10, 3, 0, 1, 2],
        [22, 23, 20, 21, 6, 7, 4, 5, 12, 13, 14, 15, 8, 9, 10, 11, 18, 19, 16, 17, 2, 3, 0, 1],
        [23, 20, 21, 22, 9, 10, 11, 8, 7, 4, 5, 6, 19, 16, 17, 18, 13, 14, 15, 12, 1, 2, 3, 0]]

def numReached(sampledCardsList):
    tries = ordered_subsets(sampledCardsList)
    reached = {0}
    for k in range(len(tries)): #tries[k] is a tuple that lists the functions
        combo = tries[k]
        #if len(combo)==7:
        #    reached.add(perm[combo[6]][ perm[combo[5]][perm[combo[4]][perm[combo[3]][perm[combo[2]][perm[combo[1]][perm[combo[0]][0]]]]]] ])
        #elif len(combo)==6:
        #        reached.add(perm[combo[5]][ perm[combo[4]][perm[combo[3]][perm[combo[2]][perm[combo[1]][perm[combo[0]][0]]]]] ])
        if len(combo)==5:
            reached.add(perm[combo[4]][perm[combo[3]][perm[combo[2]][  perm[combo[1]][perm[combo[0]][0]]  ]]])
            if len(reached)==24:
                states_reached_frequency[len(reached)-1] += 1
                return(24)
        elif len(combo)==4:
            reached.add(perm[combo[3]][perm[combo[2]][  perm[combo[1]][perm[combo[0]][0]]  ]])
            if len(reached)==24:
                states_reached_frequency[len(reached)-1] += 1
                return(24)
        elif len(combo)==3:
            reached.add(perm[combo[2]][  perm[combo[1]][perm[combo[0]][0]]  ])
        elif len(combo)==2:
            reached.add(perm[combo[1]][  perm[combo[0]][0]  ])
        elif len(combo)==1:
            reached.add(perm[combo[0]][0])
        
    states_reached_frequency[len(reached)-1] += 1    
    return(len(reached))
        

numOfCardsInHand = 5 #max of 7 right now
deck_size = 46
shift = 2
fail = 0
easy_rots = [1,2,3,4,8,12,16,20,22,1,2,3,4,8,12,16,20,22]
states_reached_frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
states_missed = []

'''
trials = 5000
success = 0
close = 0
for m in range(trials):
    cards = random.sample(range(2,47),numOfCards)
    rots =[]
    for i in range(numOfCards):
        rots.append(cards[i]//2)
#    print(rots)
    fail = fail + 24 - numReached(rots)
percentFail = fail/(23*trials)
print(percentFail) 
range(shift,deck_size+shift)
'''

for q in k_subsets(range(shift,deck_size+shift),numOfCardsInHand):
    rots = []
    for i in range(numOfCardsInHand):
        rots.append(q[i]//2)
    fail = fail + 24 - numReached(rots)
percentFail = fail/(23*comb(deck_size,numOfCardsInHand))

confirmation = 0
for k in range(24):
    states_missed.append(states_reached_frequency[k]*(23-k))
    confirmation = confirmation + states_reached_frequency[k]*(23-k)

print(fail)
print(percentFail)
print(states_reached_frequency)
print(states_missed)
print(confirmation)
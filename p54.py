### MY INCORRECT CODE

import time

t = time.time()

# T -> 10, J -> 11, Q -> 12, K -> 13, A -> 14 or 1
def valToInt(values):
    for index in range(len(values)):
        if (values[index] == "T"):
            values[index] = 10
        elif(values[index] == "J"):
            values[index] = 11
        elif(values[index] == "Q"):
            values[index] = 12
        elif(values[index] == "K"):
            values[index] = 13
        elif(values[index] == "A"):
            values[index] = 14
        else:
            values[index] = int(values[index])
    return values

def royalFlush(card_values, suits):
    values = card_values.copy()
    suit = suits[0]
    # Check if suits are the same
    for s in suits:
        if(s != suit):
            return False
    #Check for 10, 11, 12, 13, 14
    vals = [10, 11, 12, 13, 14]
    for val in values:
        if(val in vals):
            vals.remove(val)
    return len(vals) == 0

def royalFlushMax(card_values, suits):
    return [1, max(card_values)]

def straightFlush(card_values, suits):
    values = card_values.copy()
    suit = suits[0]
    for s in suits:
        if(s != suit):
            return False
    minimum = min(values)
    vals = list(range(minimum, minimum+5))
    # Check if there is an ace
    # If there is add a 1 (ace is either 14 or 1)
    if(14 in values):
        values.append(1)
    if(minimum == 2):
        vals.append(1)
        for val in values:
            if(val in vals):
                vals.remove(val)
        return len(vals) == 1
    else:
        for val in values:
            if(val in vals):
                vals.remove(val)
        return len(vals) == 0

def straightFlushMax(card_values, suits):
    return [2, max(card_values)]

def fourOfAKind(card_values, suits):
    values = card_values.copy()
    val1 = values[0]
    count1 = 0
    val2 = values[2]
    count2 = 0
    for val in values:
        if(val == val1):
            count1 += 1
        if(val == val2):
            count2 += 1
    return count1 == 4 or count2 == 4

def fourOfAKindMax(card_values, suits):
    repeat_num = 0
    for x in card_values:
        if(card_values.count(x) == 4):
            repeat_num = x
            break
    return [3, repeat_num]

def fullHouse(card_values, suits):
    values = card_values.copy()
    v = values[0]
    count = values.count(v)
    foundPair = False
    foundTriple = False
    if(count == 2):
        values.remove(v)
        values.remove(v)
        foundPair = True
    elif(count == 3):
        values.remove(v)
        values.remove(v)
        values.remove(v)
        foundTriple = True
    else:
        return False
    if(foundPair):
        v = values[0]
        count = values.count(v)
        return count == 3
    elif(foundTriple):
        v = values[0]
        count = values.count(v)
        return count == 2

def fullHouseMax(card_values, suits):
    return [4, max(card_values)]

def flush(values, suits):
    s = suits[0]
    for suit in suits:
        if(s != suit):
            return False
    return True

def flushMax(values, suits):
    return [5, max(values)]

def straight(card_values, suits):
    values = card_values.copy()
    minimum = min(values)
    vals = list(range(minimum, minimum+5))
    # Check if there is an ace
    # If there is add a 1 (ace is either 14 or 1)
    if(14 in values):
        values.append(1)
    if(minimum == 2):
        vals.append(1)
        for val in values:
            if(val in vals):
                vals.remove(val)
        return len(vals) == 1
    else:
        for val in values:
            if(val in vals):
                vals.remove(val)
        return len(vals) == 0

def straightMax(card_values, suits):
    return [6, max(card_values)]

def threeOfAKind(values, suits):
    for val in values:
        if(values.count(val) >= 3):
            return True
    return False

def threeOfAKindMax(values, suits):
    max_triple = 0
    for x in values:
        if(values.count(x) == 3):
            max_triple = x
            break
    return [7, max_triple]

def twoPairs(values, suits):
    num_pairs = 0
    for val in values:
        if(values.count(val) == 2):
            num_pairs += 1
    return num_pairs == 4

def twoPairsMax(values, suits):
    max1 = 0
    max2 = 0
    for x in values:
        if(max1 == 0 and values.count(x) == 2):
            max1 = x
        elif(values.count(x) == 2 and max1 != x):
            max2 = x
    return [8, max([max1, max2])]


def onePair(values, suits):
    for val in values:
        if(values.count(val) >= 2):
            return True
    return False

def onePairMax(values, suits):
    max_pair = 0
    for x in values:
        if(values.count(x) == 2):
            max_pair = x
            break
    return [9, max_pair]

def highestCard(cards):
    values = []
    for card in cards:
        values.append(card[0])
    values = valToInt(values)
    values.sort()
    return [10, values[0]]


# 1 -> Royal Flush, 2 -> Straight Flush, 3 -> Four of a Kind,  4 -> Full House
# 5 -> Flush,       6 -> Straight,       7 -> Three of a Kind, 8 -> Two Pairs
# 9 -> One Pair,   10 -> Highest Card
def readHand(cards):
    values = []
    suits = []
    for card in cards:
        values.append(card[0])
        suits.append(card[1])
    values = valToInt(values)
    if(royalFlush(values, suits)):      return royalFlushMax(values, suits)
    elif(straightFlush(values, suits)): return straightFlushMax(values, suits)
    elif(fourOfAKind(values, suits)):   return fourOfAKindMax(values, suits)
    elif(fullHouse(values, suits)):     return fullHouseMax(values, suits)
    elif(flush(values, suits)):         return flushMax(values, suits)
    elif(straight(values, suits)):      return straightMax(values, suits)
    elif(threeOfAKind(values, suits)):  return threeOfAKindMax(values, suits)
    elif(twoPairs(values, suits)):      return twoPairsMax(values, suits)
    elif(onePair(values, suits)):       return onePairMax(values, suits)
    else:                               return highestCard(cards)

def whoWon(p1, p2):
    values1 = []
    for card in p1:
        values1.append(card[0])
    values2 = []
    for card in p2:
        values2.append(card[0])
    values1 = valToInt(values1)
    values2 = valToInt(values2)
    values1.sort()
    values2.sort()
    for index in range(len(values1)):
        if(values1[index] > values2[index]):
            return 1
        elif(values1[index] < values2[index]):
            return 2
        else: # values1[index] == values2[index]
            continue

print("Reading in cards...")
f = open("poker.txt", "r")
cards = f.read()
f.close()
cards = cards.split("\n")
temp = []
for hands in cards:
    temp.append(hands.split(" "))
player1 = []
player2 = []
for x in temp:
    player1.append(x[0:5])
    player2.append(x[5:])
print("Checking who wins...")
player1_score = 0
player2_score = 0
for index in range(len(player1) - 1):
    p1 = readHand(player1[index])
    p2 = readHand(player2[index])
    if(p1[0] < p2[0]):
        player1_score += 1
    elif(p1[0] > p2[0]):
        player2_score += 1
    else: # p1[0] == p2[0]
        if(p1[1] > p2[1]):
            player1_score += 1
        elif(p1[1] < p2[1]):
            player2_score += 1
        else: #p1[1] == p2[1]
            answer = whoWon(player1[index], player2[index])
            if(answer == 1):
                player1_score += 1
            elif(answer == 2):
                player2_score += 1
            else:
                print("There is a problem")

print("Player 1 won %d times. Player 2 won %d times" % (player1_score, player2_score))
print("Took %.3f seconds" % (time.time() - t))

### ANSWER IS 376

### CORRECT CODE IN PYTHON 2
# from collections import Counter
#
# file_url = 'https://projecteuler.net/project/resources/p054_poker.txt'
# file = open("poker.txt", "r").read()
# hands = (line.split() for line in file)
#
# values = {r:i for i,r in enumerate('23456789TJQKA', start=2)}
# straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
# ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]
#
# def hand_rank(hand):
# 	score = zip(*sorted(((v, values[k]) for
# 		k,v in Counter(x[0] for x in hand).items()), reverse=True))
# 	score[0] = ranks.index(score[0])
# 	if len(set(card[1] for card in hand)) == 1: score[0] = 5  # flush
# 	if score[1] in straights: score[0] = 8 if score[0] == 5 else 4  # str./str. flush
# 	return score
#
# print("Project Euler 54 Solution =", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands))
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

def flush(values, suits):
    s = suits[0]
    for suit in suits:
        if(s != suit):
            return False
    return True

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

def threeOfAKind(values, suits):
    for val in values:
        if(values.count(val) >= 3):
            return True
    return False

def twoPairs(values, suits):
    num_pairs = 0
    for val in values:
        if(values.count(val) == 2):
            num_pairs += 1
    return num_pairs == 4

def onePair(values, suits):
    for val in values:
        if(values.count(val) >= 2):
            return True
    return False

def highestCard(cards):
    values = []
    for card in cards:
        values.append(card[0])
    values = valToInt(values)
    return max(values)


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
    if(royalFlush(values, suits)):      return 1
    elif(straightFlush(values, suits)): return 2
    elif(fourOfAKind(values, suits)):   return 3
    elif(fullHouse(values, suits)):     return 4
    elif(flush(values, suits)):         return 5
    elif(straight(values, suits)):      return 6
    elif(threeOfAKind(values, suits)):  return 7
    elif(twoPairs(values, suits)):      return 8
    elif(onePair(values, suits)):       return 9
    else:                               return 10

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
for index in range(len(player1)-1):
    p1 = readHand(player1[index])
    p2 = readHand(player2[index])
    if(p1 < p2):
        print(player1[index], p1, player2[index], p2)
        print("Player 1 won")
        player1_score += 1
    elif(p2 < p1):
        print(player1[index], p1, player2[index], p2)
        print("Player 2 won")
        player2_score += 1
    else: # p1 == p2
        print(player1[index], p1, player2[index], p2)
        print("Neither won")
        p1 = highestCard(player1[index])
        p2 = highestCard(player2[index])
        if(p1 > p2):
            player1_score += 1
        elif(p2 > p1):
            player2_score += 1
        else:
            print("THEY TIED???")

print("Player 1 won %d times. Player 2 won %d times" % (player1_score, player2_score))
print("Took %.ef seconds" % (time.time() - t))
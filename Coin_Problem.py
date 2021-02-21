import random as rand

# n = 1000


def Bertrand_Box_Paradox(iterations):

    box1counter = 0
    box2counter = 0
    box3counter = 0

    firstcoinpull = []
    secondcoinpull = []

    for _ in range(iterations):

        box = rand.choice(['Box1', 'Box2', 'Box3'])
        coin1choice = rand.choice([0, 1])

        if box == 'Box1':

            box1coins = ['Gold', 'Gold']
            box1counter = box1counter + 1

            coin1 = box1coins[coin1choice]
            coin2 = box1coins[coin1choice - 1]

            firstcoinpull.append(coin1)
            secondcoinpull.append(coin2)

        elif box == 'Box2':

            box2coins = ['Gold', 'Silver']
            box2counter = box2counter + 1

            coin1 = box2coins[coin1choice]
            coin2 = box2coins[coin1choice - 1]

            firstcoinpull.append(coin1)
            secondcoinpull.append(coin2)

        elif box == 'Box3':

            box3coins = ['Silver', 'Silver']
            box3counter = box3counter + 1

            coin1 = box3coins[coin1choice]
            coin2 = box3coins[coin1choice - 1]

            firstcoinpull.append(coin1)
            secondcoinpull.append(coin2)

    return [firstcoinpull, secondcoinpull, box1counter, box2counter, box3counter]


# allfirstGC = [(i, j) for i, j in zip(Bertrand_Box_Paradox(n)[0], Bertrand_Box_Paradox(n)[1]) if i == 'Gold']
# print(allfirstGC, '\n', Bertrand_Box_Paradox(n)[2], Bertrand_Box_Paradox(n)[3], Bertrand_Box_Paradox(n)[4])

# Box choice ratios (1/3)
# First coin being Gold or Silver
# Of the set where the first coin is gold (show chart showing silver and Gold second coins)


# nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration


# predesly kod nijak nemodifikujte!

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
# openFridge(fridge)

"""
Task #1
"""


def maxExpirationDay(fridge):
    max = 0
    if not fridge:
        return -1
    for i in fridge:
        if i.expiration > max:
            max = i.expiration
    return max


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""


def histogramOfExpirations(fridge):
    if not fridge or fridge == [0]:
        return []
    list = [0]
    for i in range(0, maxExpirationDay(fridge)):
        list.append(0)
    for i in range(0, len(list)):
        for j in fridge:
            if j.expiration == i:
                list[i] += 1
    return list


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]


"""
Task #3
"""


def cumulativeSum(histogram):
    list = []
    if len(histogram) == 0:
        return list
    for i in range(0, len(histogram)):
        list.append(0)
    list[0] = histogram[0]
    for i in range(1, len(histogram)):
        list[i] = histogram[i] + list[i - 1]
    return list


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(cumulativeSum([0, 2, 0, 1, 1]))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""


def sortFoodInFridge(fridge):
    list = []
    for i in fridge:
        list.append(0)
    summ = cumulativeSum(histogramOfExpirations(fridge))
    for i in fridge:
        actExp = i.expiration
        summ[actExp] -= 1
        posInd = summ[actExp]
        list[posInd] = i
    return list


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""


def reverseFridge(fridge):
    list = fridge[::-1]
    return list


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""


def eatFood(name, fridge):
    list = []
    for i in fridge:
        list.append(Food(i.name, i.expiration))
    minExp = maxExpirationDay(list)
    for i in list:
        if i.name == name and i.expiration < minExp:
            minExp = i.expiration
    for i in list:
        if i.name == name and i.expiration == minExp:
            list.remove(i)
    return list

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(
#     eatFood("donut",
#             [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#              Food("donut", 3), Food("donut", 1), Food("donut", 6)]
#             ))
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)

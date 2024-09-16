planets = ["Tatooine", "Naboo", "Hoth", "Devaron", "Dantooine", "Alderaan"]
hyperTable = [[-1, 40, 20, 150, 130, 218],
              [40, -1, 135, 70, 45, 198],
              [20, 135, -1, 20, 60, 166],
              [150, 70, 20, -1, 112, 62],
              [130, 45, 60, 112, -1, 15],
              [218, 198, 166, 62, 15, -1]]


class Jump:
    def __init__(self, sourceID, targetID, energyConsumed):
        self.sourceID = sourceID
        self.targetID = targetID
        self.energyConsumed = energyConsumed


def getPlanetIndex(planets, planetName):
    index = -1
    if planetName not in planets:
        return -1
    for i in planets:
        index += 1
        if i == planetName:
            return index


def getPlanetName(planets, planetIndex):
    length = len(planets)
    if length - 1 < planetIndex:
        return None
    return planets[planetIndex]


def getMinEnergyTargetPlanet(hyperTable, planets, planet):
    if planet not in planets:
        return None
    if len(hyperTable) != len(planets):
        return None
    index = getPlanetIndex(planets, planet)
    newTable = hyperTable[index]
    positiveValues = []
    for i in newTable:
        if i > 0:
            positiveValues.append(i)
    minElement = min(positiveValues)
    for i in range(0, len(newTable)):
        if minElement == newTable[i]:
            return planets[i]


def getAllPossibleJumps(hyperTable, sourceID, energyConsumed):
    jumpsArray = []
    for i in range(len(hyperTable[sourceID])):
        if hyperTable[sourceID][i] >= 0:
            jumpsArray.append(Jump(sourceID, i, hyperTable[sourceID][i] + energyConsumed))
    return jumpsArray


def printJumps(planets, jumpsArray):
    print("Jumps:")
    for jump in jumpsArray:
        print(
            f'{getPlanetName(planets, jump.targetID)} via {getPlanetName(planets, jump.sourceID)} for {jump.energyConsumed}')


def getMinEnergyJump(jumps):
    if jumps is None:
        return None
    energy = 0
    for i in jumps:
        if i.energyConsumed > energy:
            energy = i.energyConsumed
    for i in jumps:
        if i.energyConsumed < energy:
            energy = i.energyConsumed
    finalJump = 0
    for i in jumps:
        if i.energyConsumed == energy:
            finalJump = i
    return finalJump


def removeJump(jumps, jump):
    pass


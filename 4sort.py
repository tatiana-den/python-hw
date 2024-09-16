def sortNumbers(data, condition):
    if len(data) == 0:
        raise ValueError('Invalid input data')
    if condition == 'ASC':
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j = j - 1
            data[j + 1] = key
    elif condition == 'DESC':
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key > data[j]:
                data[j + 1] = data[j]
                j = j - 1
            data[j + 1] = key
    return data


def sortData(weights, data, condition):
    if (len(weights) == 0) or (len(data) == 0):
        raise ValueError('Invalid input data')
    if condition == 'ASC' and (len(weights) == len(data)):
        bigList = []
        for i in range(0, len(weights)):
            bigList.append([weights[i], data[i]])
        for i in range(len(bigList)):
            for j in range(0, len(bigList) - i - 1):
                if bigList[j][0] > bigList[j + 1][0]:
                    temp = bigList[j]
                    bigList[j] = bigList[j + 1]
                    bigList[j + 1] = temp
    elif condition == 'DESC' and (len(weights) == len(data)):
        bigList = []
        for i in range(0, len(weights)):
            bigList.append([weights[i], data[i]])
        for i in range(len(bigList)):
            for j in range(0, len(bigList) - i - 1):
                if bigList[j][0] < bigList[j + 1][0]:
                    temp = bigList[j]
                    bigList[j] = bigList[j + 1]
                    bigList[j + 1] = temp
    else:
        raise ValueError('Invalid input data')
    smolList = []
    for i in range(0, len(bigList)):
        smolList.append(bigList[i][1])
    return smolList

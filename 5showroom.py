class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def init(self, cars):
        for i in cars:
            self.add(i)

    def add(self, car):
        new_node = Node(None, None, car)
        if self.head is None:
            self.head = new_node
            return
        if new_node.data.price < self.head.data.price:
            tmp = self.head
            self.head = new_node
            self.head.nextNode = tmp
            tmp.prevNode = new_node
            return
        pointer = self.head
        while pointer is not None:
            if new_node.data.price >= pointer.data.price:
                if pointer.nextNode is None:
                    pointer.nextNode = new_node
                    new_node.prevNode = pointer
                    return
                pointer = pointer.nextNode
            else:
                tmp = pointer.prevNode
                tmp.nextNode = new_node
                pointer.prevNode = new_node
                new_node.nextNode = pointer
                new_node.prevNode = tmp
                return

    def findByID(self, identification):
        pointer = self.head
        while pointer is not None:
            if pointer.data.identification == identification:
                return pointer
            else:
                pointer = pointer.nextNode
        return None

    def updateName(self, identification, name):
        tmp = self.findByID(identification)
        if tmp is not None and tmp.data.identification == identification:
            tmp.data.name = name
            return tmp
        else:
            return None

    def updateBrand(self, identification, brand):
        tmp = self.findByID(identification)
        if tmp is not None and tmp.data.identification == identification:
            tmp.data.brand = brand
            return tmp
        else:
            return None

    def activateCar(self, identification):
        tmp = self.findByID(identification)
        if tmp is not None and tmp.data.identification == identification:
            tmp.data.active = True
            return tmp
        else:
            return None

    def deactivateCar(self, identification):
        tmp = self.findByID(identification)
        if tmp is not None and tmp.data.identification == identification:
            tmp.data.active = False
            return tmp
        else:
            return None

    def getDatabaseHead(self):
        return self.head

    def calculateCarPrice(self):
        pointer = self.head
        summ = 0
        while pointer is not None:
            if pointer.data.active is True:
                summ += pointer.data.price
            pointer = pointer.nextNode
        return summ

    def clean(self):
        self.head = None


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = str(name)
        self.brand = str(brand)
        self.price = int(price)
        self.active = bool(active)


db = LinkedList()


def init(cars):
    db.init(cars)


def add(car):
    db.add(car)


def updateName(identification, name):
    db.updateName(identification, name)


def updateBrand(identification, brand):
    db.updateBrand(identification, brand)


def activateCar(identification):
    db.activateCar(identification)


def deactivateCar(identification):
    db.deactivateCar(identification)


def getDatabaseHead():
    return db.getDatabaseHead()


def getDatabase():
    return db


def calculateCarPrice():
    return db.calculateCarPrice()


def clean():
    db.clean()


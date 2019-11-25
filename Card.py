class Card:

    def __init__(self,cost,name):
        self.cost = cost
        self.name = name

    def printCardInfo(self):
        print("Name: " + str(self.name))
        print("Cost: " + str(self.cost) + '\n')
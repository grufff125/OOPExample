# A minion object is a card 
from Card import Card

class Minion(Card):
    
    def __init__(self,cost,name,ATK,HP):
        Card.__init__(self,cost,name)
        self.ATK = ATK
        self.HP = HP

    def printMinionInfo(self):
        print("Name: " + str(self.name))
        print("Cost: " + str(self.cost))
        print("Attack: " + str(self.ATK))
        print("HP: " + str(self.HP) + '\n')
from Card import Card
from Minion import Minion

def main():
    townCrier = Minion(1,"Town Crier",1,2)

    redbandWasp = Minion(2,"Redband Wasp",1,3)

    warpath = Card(2,"Warpath")

    # townCrier.printCardInfo()
    townCrier.printMinionInfo()

    # redbandWasp.printCardInfo()
    redbandWasp.printMinionInfo()

    warpath.printCardInfo()

if __name__=="__main__":
    main()
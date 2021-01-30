from random import shuffle
import string
from DobbleCards import DobbleCards

margid = ["A", "B", "C", "D", "E", "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Ü","Õ","Ä",
           "Ö","X","Y","Z" ] + list(string.digits)

margidNotShuffled = ["A", "B", "C", "D", "E", "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Ü","Õ","Ä",
           "Ö","X","Y","Z" ] + list(string.digits)



def genereateCSV(numberOfSymbols,numberOfDecks,_symbols,_symbolsNotShuffled):
    for i in range(1,numberOfDecks):
        d = DobbleCards(numberOfSymbols, _symbols, True)
        d.createDeck()
        fn = "output/ee_tahed_ja_numbrid_{}_symbolit_kaardil_{}.csv".format(numberOfSymbols,i)
        d.saveAsCSV(fn,_symbolsNotShuffled)



genereateCSV(6,6,margid,margidNotShuffled)
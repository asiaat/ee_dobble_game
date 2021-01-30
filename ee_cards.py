from random import shuffle
import string
from DobbleCards import DobbleCards


numberOfSymbols = 4             # sümbolite arv kaardil
numberOfDecks   = 10            # kaardipakkide arv

alphabet = "ABCDEFGHIJKLMNOPQRSTUVÜÕÄÖXYZ"

# ainult eesti tähed
for i in range(1,numberOfDecks):
    d = DobbleCards(numberOfSymbols, list(alphabet), True)
    d.createDeck()
    fn = "output/ee_tahed_{}_symbolit_kaardil_{}.csv".format(numberOfSymbols,i)
    d.saveAsCSV(fn,list(alphabet))

# eesti tähed ja numbrid
for i in range(1,numberOfDecks):
    d = DobbleCards(numberOfSymbols, list(alphabet)+list(string.digits), True)
    d.createDeck()
    fn = "output/ee_tahed_ja_numbrid_{}_symbolit_kaardil_{}.csv".format(numberOfSymbols,i)
    d.saveAsCSV(fn,list(alphabet)+ list(string.digits))
import string
from DobbleCards import DobbleCards

ruSymbols = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") + list(string.digits)
ruSymbolsNotShuffled = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") + list(string.digits)



def genereateCSV(numberOfSymbols,numberOfDecks,_symbols,_symbolsNotShuffled):
    for i in range(1,numberOfDecks):
        d = DobbleCards(numberOfSymbols, _symbols, True)
        d.createDeck()
        fn = "output/ru_tahed_ja_numbrid_{}_symbolit_kaardil_{}.csv".format(numberOfSymbols,i)
        d.saveAsCSV(fn,_symbolsNotShuffled)



genereateCSV(6,6,ruSymbols,ruSymbolsNotShuffled)
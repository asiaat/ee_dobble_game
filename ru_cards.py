import string
from DobbleCards import DobbleCards


numberOfSymbols = 4             # sümbolite arv kaardil
numberOfDecks   = 10            # kaardipakkide arv

kirillitsa = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# ainult vene tähed
for i in range(1,numberOfDecks):
    d = DobbleCards(numberOfSymbols, list(kirillitsa), True)
    d.createDeck()
    fn = "output/ru_tahed_{}_symbolit_kaardil_{}.csv".format(numberOfSymbols,i)
    d.saveAsCSV(fn,list(kirillitsa))

# vene tähed ja numbrid
for i in range(1,numberOfDecks):
    d = DobbleCards(numberOfSymbols, list(kirillitsa)+list(string.digits), True)
    d.createDeck()
    fn = "output/ru_tahed_ja_numbrid_{}_symbolit_kaardil_{}.csv".format(numberOfSymbols,i)
    d.saveAsCSV(fn,list(kirillitsa)+ list(string.digits))





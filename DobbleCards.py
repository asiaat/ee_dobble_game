from random import shuffle


class DobbleCards:

    def __init__(self, number, _symbols, isShuffled):
        self.symbols                = _symbols
        self.symbolsNotShuffled     = _symbols
        self.numberOfSymbolsOnCard  = number
        self.cards                  = []
        self.numberOfCards          = 0
        self.cardsWithSymbols       = []
        self.shuffleSymbolsOnCard   = isShuffled


    def addFirtsSetOfCards(self):

        n = self.numberOfSymbolsOnCard - 1
        cards = []

        for i in range(n + 1):
            cards.append([1])
            for j in range(n):
                cards[i].append((j + 1) + (i * n) + 1)

        return cards

    def addSetsOfCards(self,cards):
        n = self.numberOfSymbolsOnCard - 1

        for i in range(0, n):
            for j in range(0, n):

                cards.append([i + 2])
                for k in range(0, n):
                    val = (n + 1 + n * k + (i * k + j) % n) + 1
                    cards[len(cards) - 1].append(val)

        return cards

    def shuffleCrads(self,cards):

        if self.shuffleSymbolsOnCard:
            for card in cards:
                shuffle(card)

        return cards

    def bindSymbolsToCrads(self,cards):
        shuffle(self.symbols)

        i = 0
        for card in cards:
            i += 1
            line = str(i) + " - ["
            for number in card:
                line = line + self.symbols[number - 1] + ", "
            line = line[:-2] + "]"
            print(line)

        return cards

    def createCardsWithSymbols(self,cards):
        shuffle(self.symbols)
        res = []


        i = 0
        for card in cards:
            i += 1
            line = str(i) + ";"
            for number in card:
                line = line + self.symbols[number - 1] + ";"

            line = line[:-1]
            res.append(line)


        return res


    def createDeck(self):

        self.cardsWithSymbols = self.createCardsWithSymbols(
                                self.shuffleCrads(
                                self.addSetsOfCards(
                                self.addFirtsSetOfCards()
                                )))

    def saveAsCSV(self,filename,originalSymbols):
        fh = open(filename,"w")
        for card in self.cardsWithSymbols:
            fh.writelines(card+"\n")

        fh.writelines("------------------------\n")
        fh.writelines("Kasutatud sümbolid: \n")
        fh.writelines(originalSymbols)
        fh.close()


    def saveAsChineseCSV(self,filename,originalSymbols,translation):
        fh = open(filename,"w")
        for card in self.cardsWithSymbols:
            fh.writelines(card+"\n")

        fh.writelines("------------------------\n")
        fh.writelines("Kasutatud sümbolid: \n")
        fh.writelines(originalSymbols)
        fh.writelines("\nTõlkevasted\n")

        for cchar in translation:
            fh.writelines(cchar+ ";"+translation[cchar]+ "\n")
        fh.close()









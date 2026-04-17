from Card import Card
import random

class Deck():

    def __init__(self):

        ranks=Card.RANKS
        suites=Card.SUITES
        deck=[]#datatype is an array


        for rank in ranks:
            for suite in suites:
                card=Card(suite=suite,rank=rank)
                deck.append(card)
        self.deck=deck

    
    def shuffle(self):
        newDeck=[]
        deck=self.deck
        while True:
            if len(deck)==1:
                card=deck[0]
                newDeck.append(card)
                break
            n=random.randint(0,len(deck)-1)
       
            card=deck[n] 
            deck.pop(n)
            newDeck.append(card)
        self.deck=newDeck

    def print_deck(self):
        deck=self.deck
        print("Deck size is",len(deck))
        print("..............")
        for card in deck:
            card.print_card()
            print("-------------")

#!/usr/bin/python

import random
from random import shuffle

this_deck = []
now_pl_1 = []
now_pl_2 = []

class Deck:

    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        pass

    def get_deck(self):
        the_deck = []
        temp_str = ''
        i = 0
        for x in self.RANKS:
            for y in self.SUITE:
                temp_str = x + y
                the_deck.append(temp_str)
                temp_str = ''
                
        global this_deck
        this_deck = the_deck
        return the_deck

    def shuffle_time(self, what_shuffle):
        shuffled_deck = random.sample(what_shuffle, len(what_shuffle))
        
        return shuffled_deck

    def split_the_deck(self, what_split):
        player_one = what_split[:26]
        player_two = what_split[26:]
        
        return player_one, player_two
        
            



class Player:

    def __init__(self):
        pass

    def special_case(self, i):
        global now_pl_1
        global now_pl_2

        card1_weight = 0
        card2_weight = 0
        card1_weight = this_deck.index(now_pl_1[i])
        card2_weight = this_deck.index(now_pl_2[i])

        print ('This is the WAR!!!')
        print (now_pl_1[i], now_pl_2[i])

        if len(now_pl_1[i]) == len(now_pl_2[i]):
            if len(now_pl_1[i]) == 2:
                if now_pl_1[i][0] == now_pl_2[i][0]:
                    print ('Relsing another card') #special case
                    
            elif now_pl_1[i][:2] == now_pl_2[i][:2]:
                print ('Relising another card')  #special case

        if card1_weight > card2_weight:
            print ('card1_weight')
            if now_pl_2[i] and now_pl_2[i+1] and now_pl_2[i+2]:
                now_pl_1.append(now_pl_2[i])
                now_pl_1.append(now_pl_2[i+1])
                now_pl_1.append(now_pl_2[i+2])
                now_pl_2.remove(now_pl_2[i])
                now_pl_2.remove(now_pl_2[i])
                now_pl_2.remove(now_pl_2[i])
                print ('Player 1 (Comp) gets 3 cards')
                self.play_cards()
            else:
                print ("Player 1 (Comp) is the winner...")
            
        elif card1_weight < card2_weight:
            print ('card2_weight')
            if now_pl_1[i] and now_pl_1[i+1] and now_pl_1[i+2]:
                now_pl_2.append(now_pl_1[i])
                now_pl_2.append(now_pl_1[i+1])
                now_pl_2.append(now_pl_1[i+2])
                now_pl_1.remove(now_pl_1[i])
                now_pl_1.remove(now_pl_1[i])
                now_pl_1.remove(now_pl_1[i])          
                print ('Player 2 (You) get 3 cards')
                self.play_cards()
            else:
                print ("Player 2 (You) is the winner...")
        

    
    def compare_cards(self, card_1, card_2):
        global this_deck
        global now_pl_1
        global now_pl_2
        
        card1_weight = 0
        card2_weight = 0
        card1_weight = this_deck.index(card_1)
        card2_weight = this_deck.index(card_2)

        if len(card_1) == len(card_2):
            if len(card_1) == 2:
                if card_1[0] == card_2[0]:
                    print ('special case')  #special case
                    self.special_case(1)
                    
            elif card_1[:2] == card_2[:2]:
                print ('special case' + card_1[:2])  #special case
                self.special_case(1)
                
        if card1_weight > card2_weight:
            now_pl_1.append(card_2)
            now_pl_2.remove(card_2)
            print ('Player 1 (Comp) get the card')
            self.play_cards()
            
        elif card1_weight < card2_weight:
            now_pl_2.append(card_1)
            now_pl_1.remove(card_1)
            print ('Player 2 (You) get the card')
            self.play_cards()
        
    def play_cards(self):
        global now_pl_1
        global now_pl_2
        
        if len(now_pl_1) >= 1 and len(now_pl_2) >= 1:   #both players have cards
            print (now_pl_1[0], now_pl_2[0])
            self.compare_cards(now_pl_1[0], now_pl_2[0])
            
        elif len(now_pl_1) >= 1:    #Player 2 has no cards
            print ("Player 1 (Comp) is the winner!!!")
            
        
        else:   # Player 1 has no cards
            print ("Player 2 (You) is the winner!!!")
            
            
        

from_deck = Deck()
xr = from_deck.get_deck() 
sh = from_deck.shuffle_time(xr)
sp = from_deck.split_the_deck(sh)

now_pl_1 = sp[0]
now_pl_2 = sp[1]

from_play = Player()
pl = from_play.play_cards() # launching the game


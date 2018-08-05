#!/usr/bin/python

import random
from random import shuffle


class Deck:

    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        pass

    def get_deck(self):
        the_deck = []
        temp_str = ''
        for x in self.RANKS:
            for y in self.SUITE:
                temp_str = x + y
                the_deck.append(temp_str)
                temp_str = ''

        return the_deck

    def shuffle_time(self, what_shuffle):
        shuffled_deck = random.sample(what_shuffle, len(what_shuffle))
        return shuffled_deck

    def split_the_deck(self, what_split):
        player_one = what_split[:18]
        player_two = what_split[18:]

        return player_one, player_two
        
            



class Hand:

    def __init__(self):
        pass

results = Deck()
xr = results.get_deck() 
sh = (results.shuffle_time(xr))
print (results.split_the_deck(sh))

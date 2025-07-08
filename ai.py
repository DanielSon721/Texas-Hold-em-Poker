from collections import defaultdict
from typing import List
from card import Card
import random

class AI:

    card1 = None
    card2 = None
    confidence = 0
    money = 1000
    folded = False
    ranking = 0
    kicker1 = 0
    kicker2 = 0

    def set_cards(self, card1: Card, card2: Card) -> None:
        self.card1 = card1
        self.card2 = card2
        self.confidence = card1.get_number() + card2.get_number()

        if card1.get_number() == card2.get_number():
            self.confidence += 4
        if card1.get_suit() == card2.get_suit():
            self.confidence += 2
        if abs(card1.get_number() - card2.get_number()) < 5:
            self.confidence += 1
    
    def bet(self) -> bool:
        x = random.randint(1, 25)
        if (x <= self.confidence):
            return True
        else:
            return False

    def get_cards(self) -> str:
        return self.card1.__str__() + " " + self.card2.__str__()
    
    def get_card1(self) -> Card:
        return self.card1
    
    def get_card2(self) -> Card:
        return self.card2
    
    def get_money(self) -> int:
        return self.money;
    
    def set_folded(self, boolean: bool) -> None:
        self.folded = boolean
    
    def is_folded(self) -> bool:
        return self.folded
    
    def withdraw(self, amount: int) -> None:
        self.money -= amount
    
    def reset_kickers(self) -> None:
        self.kicker1 = 0
        self.kicker2 = 0
    
    def calculate_rank(self, hand_combo: List[Card]) -> int:

        self.ranking = 1
        self.reset_kickers()

        #1 = high card
		#2 = pair
		#3 = two pair
		#4 = three of a kind
		#5 = straight
		#6 = flush
		#7 = full house
		#8 = four of a kind
		#9 = straight flush
		#10 = royal flush

        number_map = defaultdict(int)
        suit_map = defaultdict(int)

        #counts number
        for i in range (len(hand_combo)):
            number_map[hand_combo[i].get_number()] += 1
        #counts suit
        for i in range (len(hand_combo)):
            suit_map[hand_combo[i].get_suit()] += 1
        
        if 2 in number_map.values():
            self.ranking = 2 #pair
        if self.is_two_pair(number_map):
            self.ranking = 3 #two-pair
        if 3 in number_map.values():
            self.ranking = 4 #three of a kind
        if self.is_straight(sorted(hand_combo), number_map):
            self.ranking = 5 #straight
        if 5 in suit_map.values() or 6 in suit_map.values() or 7 in suit_map.values():
            self.ranking = 6 #flush
        if 2 in number_map.values() and 3 in number_map.values():
            self.ranking = 7 #full house
        if 4 in number_map.values():
            self.ranking = 8 #four of a kind
        if self.is_straight_flush(sorted(hand_combo), suit_map):
            self.ranking = 9 #straight flush
        if self.is_royal_flush(self.ranking == 9):
            self.ranking = 10 #royal flush
        
        return self.ranking

    #checks two pair
    def is_two_pair(self, number_map):
        pairs = 0
        for value in number_map.values():
            if value == 2:
                pairs += 1
        
        return pairs > 1
    
    #checks straight
    def is_straight(self, hand_combo: List[Card], number_map: defaultdict[int, int]):

        if 14 in number_map:
            hand_combo.insert(0, Card(1, hand_combo[len(hand_combo) - 1].get_suit()))
            number_map[1] = 1

        numbers = sorted(number_map.keys())
        
        for i in range(len(numbers) - 1, 3, -1):
            if (numbers[i] - 4 == numbers[i - 4]):
                self.kicker1 = numbers[i]
                return True
        
        return False
    
    #checks straight flush
    def is_straight_flush(self, hand_combo: List[Card], suit_map: defaultdict[int, int]):

        mode_suit = 0

        for suit in suit_map.keys():
            if suit_map[suit] >= 5:
                mode_suit = suit
                break
        
        if mode_suit == 0:
            return False

        for i in range(len(hand_combo) - 1, -1, -1):
            if hand_combo[i].get_suit() != mode_suit:
                hand_combo.pop(i)
        
        number_map = defaultdict(int)

        #counts number
        for i in range (len(hand_combo)):
            number_map[hand_combo[i].get_number()] += 1
        
        return self.is_straight(hand_combo, number_map)

    def is_royal_flush(self, straight_flush: bool):
        return straight_flush and self.kicker1 == 14


    #removes duplicate numbers
    def remove_duplicates(self, number_map):
        return number_map.keys()
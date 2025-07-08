

class Card:
    #1 = diamonds
    #2 = hearts
    #3 = spades
    #4 = clubs

    number = 0
    suit = 0

    def __init__(self, number: int, suit: int) -> None:
        self.number = number
        self.suit = suit
    
    def get_number(self) -> int:
        return self.number

    def get_suit(self) -> int:
        return self.suit
    
    def __lt__(self, other) -> bool:
        return self.number < other.number
    
    def __str__(self) -> str:

        output = ""

        if self.number == 11:
            output += 'J'
        elif self.number == 12:
            output += 'Q'
        elif self.number == 13:
            output += 'K'
        elif self.number == 14:
            output += 'A'
        else:
            output += str (self.number)
        
        if self.suit == 1:
            output += "\u2666"
        elif self.suit == 2:
            output += "\u2764"
        elif self.suit == 3:
            output += "\u2660"
        elif self.suit == 4:
            output += "\u2663"
        
        return output
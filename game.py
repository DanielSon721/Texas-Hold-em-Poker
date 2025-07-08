import random

from ai import AI
from card import Card

def main():
    ai_array = []
    player_money = 1000

    print("How many opponents would you like?: ", end = "")
    number_of_opponents = int (input())

    for i in range(number_of_opponents):
        ai_array.append(AI())

    while (player_money > 0):

        print("NEW GAME")

        pot = 0

        deck_of_cards = []

        #creates deck of cards
        for i in range(1, 5):
            for j in range(2, 15):
                deck_of_cards.append(Card(j, i))
        
        # for c in deck_of_cards:
        #     print(c)

        #assigns cards to player
        x = random.randint(0, len(deck_of_cards) - 1)
        player_card1 = deck_of_cards[x]
        deck_of_cards.pop(x)

        x = random.randint(0, len(deck_of_cards) - 1)
        player_card2 = deck_of_cards[x]
        deck_of_cards.pop(x)

        #assigns cards to ai
        for i in range(len(ai_array)):

            ai_array[i].set_folded(False)

            x = random.randint(0, len(deck_of_cards) - 1)
            card1 = deck_of_cards[x]
            deck_of_cards.pop(x)

            x = random.randint(0, len(deck_of_cards) - 1)
            card2 = deck_of_cards[x]
            deck_of_cards.pop(x)

            ai_array[i].set_cards(card1, card2)

        #FLOP
        x = random.randint(0, len(deck_of_cards) - 1)
        flop1 = deck_of_cards[x]
        deck_of_cards.pop(x)
        x = random.randint(0, len(deck_of_cards) - 1)
        flop2 = deck_of_cards[x]
        deck_of_cards.pop(x)
        x = random.randint(0, len(deck_of_cards) - 1)
        flop3 = deck_of_cards[x]
        deck_of_cards.pop(x)


        print_information(ai_array, player_card1, player_card2, player_money, pot, flop1, flop2, flop3, None, None, False)

        #players move (flop)
        print("Would you like to bet 25 cents? (Y/N): ", end = "")
        if input() == "N":
            continue
        pot += 25
        player_money -= 25
        print("\nYou bet 25 cents")

        #opponents move
        pot += opponents_moves(ai_array)
        


        #TURN
        x = random.randint(0, len(deck_of_cards) - 1)
        turn = deck_of_cards[x]
        deck_of_cards.pop(x)

        print_information(ai_array, player_card1, player_card2, player_money, pot, flop1, flop2, flop3, turn, None, False)

        #players move (turn)
        print("Would you like to bet 25 cents? (Y/N): ", end = "")
        if input() == "N":
            continue
        pot += 25
        player_money -= 25
        print("\nYou bet 25 cents")

        #opponents move
        pot += opponents_moves(ai_array)
        


        #RIVER
        x = random.randint(0, len(deck_of_cards) - 1)
        river = deck_of_cards[x]
        deck_of_cards.pop(x)

        print_information(ai_array, player_card1, player_card2, player_money, pot, flop1, flop2, flop3, turn, river, False)

        #players move (river)
        print("Would you like to bet 25 cents? (Y/N): ", end = "")
        if input() == "N":
            continue
        pot += 25
        player_money -= 25
        print("\nYou bet 25 cents")

        #opponents move
        pot += opponents_moves(ai_array)

        

        #prints ranks
        print_information(ai_array, player_card1, player_card2, player_money, pot, flop1, flop2, flop3, turn, river, True)
        hand_combo = [flop1, flop2, flop3, turn, river]
        print_ranks(ai_array, hand_combo)
        print("\n\n")




def opponents_moves(ai_array):

    pot = 0

    for i in range(len(ai_array)):
        if ai_array[i].is_folded():
            continue
        if ai_array[i].bet():
            print("Opponent " + str (i + 1) + " bet 25 cents")
            pot += 25
            ai_array[i].withdraw(25)
        else:
            print("Opponent " + str (i + 1) + " folded")
            ai_array[i].set_folded(True)
    
    print("")
    return pot



def print_information(ai_array, player_card1, player_card2, player_money, pot, flop1, flop2, flop3, turn, river, end):

    print("Information: (Pot: " + str (pot) + ")")

    #prints ai information
    for i in range(len(ai_array)):
        if ai_array[i].is_folded():
            continue
        print("Opponent " + str (i + 1) + ":\t" + ai_array[i].get_cards() + "\tMoney: " + str (ai_array[i].get_money()))
    
    #prints player information
    print("You:\t\t" + player_card1.__str__() + " " + player_card2.__str__() + "\tMoney: " + str (player_money) + "\n")

    if not turn:
        print("Flop: " + flop1.__str__() + " " + flop2.__str__() + " " + flop3.__str__() + "\n")
    elif not river:
        print("Turn: " + flop1.__str__() + " " + flop2.__str__() + " " + flop3.__str__() + " " + turn.__str__() + "\n")
    elif end:
        print("River: " + flop1.__str__() + " " + flop2.__str__() + " " + flop3.__str__() + " " + turn.__str__() + " " + river.__str__() + "\n")
    else:
        print("River: " + flop1.__str__() + " " + flop2.__str__() + " " + flop3.__str__() + " " + turn.__str__() + " " + river.__str__() + "\n")
    
    

def print_ranks(ai_array, hand_combo) -> None:
    for i in range(len(ai_array)):
        if ai_array[i].is_folded():
            continue
        print("Opponent " + str (i + 1) + ": ", end = "")
        hand_combo.append(ai_array[i].get_card1())
        hand_combo.append(ai_array[i].get_card2())
        x = ai_array[i].calculate_rank(hand_combo)
        hand_combo.pop(6)
        hand_combo.pop(5)
        if x == 1:
            print("High card")
        elif x == 2:
            print("Pair")
        elif x == 3:
            print("Two pair")
        elif x == 4:
            print("Three of a kind")
        elif x == 5:
            print("Straight")
        elif x == 6:
            print("Flush")
        elif x == 7:
            print("Full house")
        elif x == 8:
            print("Four of a kind")
        elif x == 9:
            print("Straight flush")
        elif x == 10:
            print("Royal flush")
    



if __name__ == "__main__":
    main()
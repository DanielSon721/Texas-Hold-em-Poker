import random
import time

from ai import AI
from card import Card


def opponents_moves(ai_array):

    pot = 0

    print("")

    for i in range(len(ai_array) - 1):
        if ai_array[i].is_folded():
            continue
        if ai_array[i].bet():
            print(f"{ai_array[i].get_name()} bet 25 cents")
            pot += 25
            ai_array[i].withdraw(25)
            time.sleep(.1)
        else:
            print(f"{ai_array[i].get_name()} folded")
            ai_array[i].set_folded(True)
            time.sleep(.1)

    print(f"{ai_array[-1].get_name()} bet 25 cents\n")
    pot += 25
    ai_array[-1].withdraw(25)

    time.sleep(.5)

    return pot



def print_information(ai_array, pot, flop1, flop2, flop3, turn, river, end):

    print("------------------------------------")
    print(f"Information: (Pot: {pot})")
    time.sleep(.3)

    #prints ai information
    for i in range(len(ai_array) - 1):
        if ai_array[i].is_folded():
            continue
        if end:
            print(f"{ai_array[i].get_name()}:\t{ai_array[i].get_cards()}\tMoney: {ai_array[i].get_money()}")
            time.sleep(.1)
        else:
            print(f"{ai_array[i].get_name()}:\t\U0001F0A0 \U0001F0A0\tMoney: {ai_array[i].get_money()}")
            time.sleep(.1)
    
    #prints player information
    print(f"{ai_array[-1].get_name()}:\t\t{ai_array[-1].get_cards()}\tMoney: {ai_array[-1].get_money()}\n")

    if not turn:
        time.sleep(.5)
        print(f"Flop: {flop1.__str__()} {flop2.__str__()} {flop3.__str__()}")
    elif not river:
        time.sleep(.5)
        print(f"Turn: {flop1.__str__()} {flop2.__str__()} {flop3.__str__()} {turn.__str__()}")
    else:
        time.sleep(.5)
        print(f"River: {flop1.__str__()} {flop2.__str__()} {flop3.__str__()} {turn.__str__()} {river.__str__()}")
    
    time.sleep(1)

    print("------------------------------------\n")
    
    

def print_ranks(ai_array, hand_combo) -> None:
    for i in range(len(ai_array)):
        if ai_array[i].is_folded(): # skip folded players
            continue
        print(f"{ai_array[i].get_name()}: ", end = "")

        # calculates rank
        hand_combo.append(ai_array[i].get_card1())
        hand_combo.append(ai_array[i].get_card2())
        rank = ai_array[i].calculate_rank(hand_combo)
        hand_combo.pop(6)
        hand_combo.pop(5)

        if rank == 1:
            print("High card")
        elif rank == 2:
            print("Pair")
        elif rank == 3:
            print("Two pair")
        elif rank == 4:
            print("Three of a kind")
        elif rank == 5:
            print("Straight")
        elif rank == 6:
            print("Flush")
        elif rank == 7:
            print("Full house")
        elif rank == 8:
            print("Four of a kind")
        elif rank == 9:
            print("Straight flush")
        elif rank == 10:
            print("Royal flush")
        
        time.sleep(.1)
    



if __name__ == "__main__":

    ai_array = []

    number_of_opponents = int (input("\nHow many opponents would you like?: "))
    time.sleep(1)

    # creates ai opponenets
    for i in range(number_of_opponents):
        ai_array.append(AI("Opponent " + str(i+1)))
    # player
    ai_array.append(AI("You"))

    while (ai_array[-1].get_money() > 0):

        print("\n\n\t      --------")
        print("\t      NEW GAME")
        print("\t      --------\n")
        time.sleep(1)

        pot = 0

        deck_of_cards = []

        #creates deck of cards
        for i in range(1, 5): # suit
            for j in range(2, 15): # denomination 2-Ace
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

        # sets players cards
        ai_array[-1].set_cards(player_card1, player_card2)
        ai_array[-1].set_folded(False)

        #assigns cards to ai
        for i in range(number_of_opponents):

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


        print_information(ai_array, pot, flop1, flop2, flop3, None, None, False)

        #players move (flop)
        print("Would you like to bet 25 cents? (Y/N): ", end = "")
        if input() == "N":
            continue
        time.sleep(.5)

        #opponents move
        pot += opponents_moves(ai_array)
        


        #TURN
        x = random.randint(0, len(deck_of_cards) - 1)
        turn = deck_of_cards[x]
        deck_of_cards.pop(x)

        print_information(ai_array, pot, flop1, flop2, flop3, turn, None, False)

        #players move (turn)
        print("Would you like to bet 25 cents? (Y/N): ", end = "")
        if input() == "N":
            continue
        time.sleep(.5)

        #opponents move
        pot += opponents_moves(ai_array)
        


        #RIVER
        x = random.randint(0, len(deck_of_cards) - 1)
        river = deck_of_cards[x]
        deck_of_cards.pop(x)

        print_information(ai_array, pot, flop1, flop2, flop3, turn, river, False)

        #players move (river)
        print("Would you like to bet 25 cents? (Y/N): ", end = "")
        if input() == "N":
            continue
        time.sleep(.5)

        #opponents move
        pot += opponents_moves(ai_array)

        

        #prints ranks
        print_information(ai_array, pot, flop1, flop2, flop3, turn, river, True)
        hand_combo = [flop1, flop2, flop3, turn, river]
        print_ranks(ai_array, hand_combo)
# Author: Nick Fan
# Date: 1/24/2023
# Description: Test file for my_cards

from my_cards import *

def main() -> None:
    ace_club = Card(1, 1)
    two_diamond = Card(2, 2)
    three_heart = Card(3, 3)
    four_spade = Card(4, 4)
    five_club = Card(5, 1)
    six_diamond = Card(6, 2)
    seven_heart = Card(7, 3)
    eight_spade = Card(8, 4)
    nine_club = Card(9, 1)
    ten_diamond = Card(10, 2)
    jack_heart = Card(11, 3)
    queen_spade = Card(12, 4)
    king_club = Card(13, 1)
    king_diamond = Card(13, 2)
    print(f"King of Clubs is equal to King of Diamonds: {king_club == king_diamond}")
    print(f"King is equal to Queen {king_diamond == queen_spade}")
    print(f"King is greater than Queen: {king_diamond > queen_spade}")
    print(f"Queen is less than King: {queen_spade > king_diamond}")
    print(f"Same suite (K C, 5 C, Q S): {same_suite(king_diamond, five_club, queen_spade)}")
    cards = [ace_club, two_diamond, three_heart, four_spade, five_club, six_diamond, seven_heart]
    cards2 = [eight_spade, nine_club, ten_diamond, jack_heart, queen_spade, king_club]
    print(display_cards(card_labels=cards))
    print(display_cards(card_labels=cards2))
    print(display_cards(ace_club, jack_heart, queen_spade, king_club))
    print(display_cards(card_labels=(1, "Q2", 10, "D H", "ABCDE"), format=False))

if __name__ == "__main__":
    main()
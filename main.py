# Author: Nick Fan
# Date: 1/24/2023
# Description: Test file for my_cards

from my_cards import *

def main() -> None:
    ace = Card(1, 1)
    tw = Card(2, 2)
    th = Card(3, 3)
    fo = Card(4, 4)
    fi = Card(5, 1)
    si = Card(6, 2)
    se = Card(7, 3)
    e = Card(8, 4)
    n = Card(9, 1)
    t = Card(10, 2)
    j = Card(11, 3)
    q = Card(12, 4)
    k = Card(13, 1)
    k2 = Card(13, 2)
    print(f"King of Clubs is equal to King of Diamonds: {k == k2}")
    print(f"King is equal to Queen {k == q}")
    print(f"King is greater than Queen: {k > q}")
    print(f"Queen is less than King: {q > k}")
    print(f"Same suite (K C, 5 C, Q S): {same_suite(k, fi, q)}")
    cards = [ace, tw, th, fo, fi, si, se, e, n, t, j, q, k]
    print(display_cards(card_labels=cards))
    print(display_cards(ace, j, q, k))
    print(display_cards(card_labels=(1, "Q2", 10, "D H", "ABCDE"), format=False))

if __name__ == "__main__":
    main()
''' A module to indicate card values allowing for formatted display.

Written by: Nick Fan
Date: 1/25/2023

Classes:
    Card:
        card_value_translator:
            Generates the value of the given integer as a card label representation.
        card_suite_translator:
            Generates the value of the given integer as a card label representation.

Functions:
	same_suite - Checks whether two or more cards are of the same suite.
    display_cards - Returns display of n number of cards as string.

Usage: in your program, import the my_cards module. Then create card objects or call a function.

Example Usage:

	from my_cards import Card
    from my_cards import display_cards

    card_value = 13
    card_suite = 2
    new_card = Card(13, 2)

	print(display_cards(new_card))
'''

# Card Class --------------------------------------------------------------|
class Card():
    '''
    A class to represent cards.
    '''

    def __init__(self, value: int, suite: str) -> None:
        '''
        Create a card object.
            Args:
                value: value of the card, between 1 to 13, inclusive.
                suite: suite of the card, between 1 to 4, inclusive.
            Returns:
                None
            Raises:
                ValueError if card value is < 1 or > 13 and if suite < 1 or > 4.
            Suites are as follows: 1 - Clubs, 2 - Diamonds,
            3 - Hearts, 4 - Spades
        '''
        if value < 1 or value > 13:
            raise ValueError("Card value must be between 1 and 13.")
        if suite < 1 or suite > 4:
            raise ValueError("Suite must be between 1 and 4.")
        # Indicates numerical representations
        self.true_value = value
        self.true_suite = suite
        # Indicates card value representations
        self.value = self.card_value_translator(value)
        self.suite = self.card_suite_translator(suite)

    @staticmethod
    def card_value_translator(value: int) -> object:
        '''
        Generates the value of the given integer as a card label representation.
            Args:
                Any integer between 1 and 13, inclusive.
            Returns:
                The value of the integer as a card label representation.
            Raises:
                ValueError if card value is < 1 or > 13.
        '''
        if value > 13 or value < 1:
            raise ValueError("Card value must be in range 1-13.")
        if value <= 10 and value != 1:
            return value
        if value == 1:
            return 'A'
        if value == 11:
            return 'J'
        if value == 12:
            return 'Q'
        return 'K'

    @staticmethod
    def card_suite_translator(suite: int) -> str:
        '''
        Generates the value of the given integer as a card label representation.
            Args:
                Any integer between 1 and 13, inclusive.
            Returns:
                The value of the integer as a card label representation.
            Raises:
                ValueError if the suite value is < 1 or > 4.
        '''
        if suite > 4 or suite < 1:
            raise IndexError("Out of bounds, must be in range 1-4.")
        if suite == 1:
            return 'C'
        if suite == 2:
            return 'D'
        if suite == 3:
            return 'H'
        return 'S'

    def __lt__(self, other) -> bool:
        return self.true_value < other.true_value

    def __gt__(self, other) -> bool:
        return self.true_value > other.true_value

    def __eq__(self, other) -> bool:
        return self.true_value == other.true_value

    def __ne__(self, other) -> bool:
        return self.true_value != other.true_value

    def __str__(self):
        return f"Value: {self.value}, Suite: {self.suite}"


# Related Functions -------------------------------------------------------|
def same_suite(card: Card, *cards: Card) -> bool:
    '''
    Checks whether two or more cards are of the same suite.
        Args:
            card: Any card object
            cards: Any other card objects
        Returns:
            True if cards are of the same suite
            False if cards are not all of the same suite
    '''
    for other in cards:
        if card.suite == other.suite:
            continue
        return False
    return True

def display_cards(*cards: Card, card_labels=None, format=True) -> str:
    '''
    Returns display of n number of cards as string.
        Args:
            cards: Any number of card objects.
            labels: Any iterable of card objects or labels.
            format: Indicates if parameters are all
            card objects (True) or not (False).
        Returns:
            String formatted card display for given cards.
        Raises:
            TypeError if too many argument types are passed.
            ValueError if a given label is too large to fit on the card.
    '''
    top_bot = ""
    borders = ""
    labels = ""
    if format:
        if card_labels and cards:
            raise TypeError("Too many argument types, only 1 can be used.")
        if card_labels:
            this_cards = card_labels
        else:
            this_cards = cards

        for card in this_cards:
            top_bot += "+-----+   "
            borders += "|     |   "
            try:
                if int(card.value) == 10:
                    labels += f"| {card.value}{card.suite} |   "
                else:
                    labels += f"| {card.value} {card.suite} |   "
            except ValueError:
                labels += f"| {card.value} {card.suite} |   "
    else:
        for val in card_labels[:-1]:
            if len(str(val)) > 5:
                raise ValueError(f"Label \"{val}\" is too large to fit on card.")
            top_bot += "+-----+   "
            borders += "|     |   "
            labels += f"|{val:^5}|   "
        top_bot += "+-----+"
        borders += "|     |"
        labels += f"|{card_labels[-1]:^5}|"
    top_bot, borders, labels = top_bot + "\n", borders + "\n", labels + "\n"
    return top_bot + borders + labels + borders + top_bot

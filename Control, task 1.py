class Card_enter:
    def __init__(self, card):
        self.card = card

    def enter_card(self):

        print(12 * '*', self.card[14:])


card = Card_enter(input('enter you card: '))

card.enter_card()
############################################################# TASK 1 ############################################################
# class Card_enter:
#     def __init__(self, card):
#         self.card = card
#
#     def enter_card(self):
#
#         print(12 * '*', self.card[14:])
#
#
# card = Card_enter(input('enter you card: '))
#
# card.enter_card()

############################################################# TASK 2 ############################################################
# class Polindrom:
#     def __init__(self, words):
#         self.words = words
#
#     def polindrom_rly(self):
#         if self.words[::-1] == self.words:
#             print('True')
#         else:
#             print('False')
#
#
# string = Polindrom(input().lower())
#
# string.polindrom_rly()
############################################################# TASK 3 ############################################################
class Tomato:
    states = {1: 'green', 2: 'yellow', 3: 'red'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
            print(f'Tomato {self._index} на {self._state} стадии созревания')

    def is_ripe(self):
        if self._state == 3:
            print('Созрел')
        else:
            print('Ещё несозрел')


class TomatoBush:
    def __init__(self, count):
        self.count = count
        self.tomatoes = []

    def add(self):
        for i in range(self.count):
            self.tomatoes.append(self.tomatoes)

    def info_tomato(self):
        print(self.tomatoes)

    def growAll(self):
        for tomato in self.tomatoes:
            tomato.next_state()

    def info_state(self, index):
        self.tomatoes[index].is_ripe()


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.growAll()
        print('Растения улучшились')

    def harvest(self):
        if self._plant.growAll():
            self.tomatoes = []
            print('Весь урожай собран, милорд')
        else:
            print('Томаты ещё зелёные')

    @staticmethod
    def knowledge_base():
        print('All is Ripe?)')


tomat = Tomato("Axwl")
tomat.grow()
tomat.is_ripe()
Gardener.knowledge_base()
Many_tomato = TomatoBush(8)
gardener = Gardener('Алёшенька', Many_tomato)
gardener.work()
gardener.work()
gardener.harvest()

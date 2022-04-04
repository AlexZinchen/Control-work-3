class Polindrom:
    def __init__(self, words):
        self.words = words

    def polindrom_rly(self):
        if self.words[::-1] == self.words:
            print('True')
        else:
            print('False')


string = Polindrom(input().lower())

string.polindrom_rly()
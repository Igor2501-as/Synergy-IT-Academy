С
использованием
ООП
написать
программу, которая
раздает
карты
для
игры
в
дурака

1.
Реализовать
класс
карты
как
масть + значение, метод
__repr__
и
__str__
для
вывода
на
экран


class Card(object):
    SPADE = 1

    HEARTS = 2

    CLOVER = 3

    DIAMOND = 4

    def __init__(self, suit, value):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __lt__(self):
        pass

    def __eq__(self):
        pass


2.
Класс
колоды

а) в
конструкторе
наполнение
полной
колодой
или
картами
из
конструктора

б) метод
перемешивания
колоды, метод
извлечения
случайной
карты

в) метод
__str__
для
вывода
на
экран


class CardDeck(self):

    def __init__(self, cards=None):

        if cards is None:

            self._cards = self._get_full_deck()

        else:

            self._cards = cards

    def __str__(self):

        '''

        String representation of Deck

        '''

    def shuffle(self):

        '''

        Randomly shuffle cards in deck

        '''

        pass

    def pick_first(self):

        '''

        remove first card in dec and return it

        '''

        pass

    def _get_full_deck(self):

        '''

        Generate list of 36 cards

        '''

        pass


3.
Функцию
начала
игры
в
дурака

а) чтение
с
клавиатуры
кол - ва
игроков.

    б) используя
класс
из
2.
случайно
раздать
игракам
колоды
по
6
карт

в) случайно
выбрать
одну
карту
из
колоды
как
козырь

г) определить
кто
ходит
первым, вывести
колоды
игроков
на
экран


def get_player_deck(card_deck):
    '''

    Using Full deck create deck for particular player

    '''

    pass


def print_players(players):
    '''

    Print players decks to screen

    '''

    pass


def get_first_player(players, trump):
    '''

    Select player who will play frist

    '''

    pass


def main():
    full_deck = CardDeck()

    num_players = int(input('Enter num players'))

    players = [get_player_deck(full_deck) for i in range(num_players)]

    print_players(player)

    trump = ...

    first_player = get_first_player(players, trump)


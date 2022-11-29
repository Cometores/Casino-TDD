# Упражнение 2. Ставки
# Я, как игрок, могу купить фишки у казино, чтобы делать ставки
# Я, как игрок, могу сделать ставку в игре в кости, чтобы выиграть
# Я, как игрок, не могу поставить фишек больше, чем я купил
# Я, как игрок, могу сделать несколько ставок на разные числа, чтобы повысить вероятность выигрыша
# Я, как казино, принимаю только ставки, кратные 5
# Я, как игрок, могу поставить только на числа 1 - 6

import unittest

from casino.casino import Player, Game


class TestTwo(unittest.TestCase):
    def test_player_can_buy_chips(self):
        player_Alex = Player()
        chips_to_buy = 600

        player_Alex.buy_chips(chips_to_buy)

        self.assertEqual(chips_to_buy, player_Alex.get_chips(), "The player could not buy the right amount of chips")

    def test_player_can_bet_in_game_of_dice(self):
        player_Alex = Player()
        game = Game()
        game.add_player(player_Alex)
        chips_to_bet = 200
        player_Alex.buy_chips(chips_to_bet)

        player_Alex.bet(chips_to_bet, 6)

        self.assertEqual(0, player_Alex.get_chips(), "The player should not have any chips left")
        self.assertEqual(0, game.players_list[game.players_list.index(player_Alex)].get_chips(),
                         "The player should not have any chips left")
        self.assertEqual(200, player_Alex.get_bet(6), "A bet is made incorrectly")

    def test_player_can_not_bet_more_chips_than_he_bought(self):
        player_Alex = Player()
        game = Game()
        game.add_player(player_Alex)
        chips_to_buy = 200
        player_Alex.buy_chips(chips_to_buy)

        with self.assertRaises(Exception):
            player_Alex.bet(300, 5)

        with self.assertRaises(Exception):
            player_Alex.bet(300, 5)

    def test_player_can_bet_on_different_numbers(self):
        player_Alex = Player()
        game = Game()
        game.add_player(player_Alex)
        chips_to_buy = 400
        player_Alex.buy_chips(chips_to_buy)

        player_Alex.bet(50, 1)
        player_Alex.bet(200, 3)
        player_Alex.bet(150, 1)

        self.assertEqual(200, player_Alex.get_bet(3))
        self.assertEqual(200, player_Alex.get_bet(1))

    def test_casino_only_accepts_bets_in_multiples_of_five(self):
        player_Alex = Player()
        game = Game()
        game.add_player(player_Alex)
        chips_to_buy = 400
        player_Alex.buy_chips(chips_to_buy)

        with self.assertRaises(Exception):
            player_Alex.bet(1, 1)

        with self.assertRaises(Exception):
            player_Alex.bet(12, 5)

    def test_player_can_bet_on_numbers_from_one_to_six(self):
        player_Alex = Player()
        game = Game()
        game.add_player(player_Alex)
        chips_to_buy = 400
        player_Alex.buy_chips(chips_to_buy)

        with self.assertRaises(Exception):
            player_Alex.bet(100, 7)

        with self.assertRaises(Exception):
            player_Alex.bet(100, 89)

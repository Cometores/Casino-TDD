# Упражнение 3. Выигрыш/проигрыш
# Я, как игрок, могу проиграть, если сделал неправильную ставку
# Я, как игрок, могу выиграть 6 ставок, если сделал правильную ставку
# Я, как казино, получаю фишки, которые проиграл игрок
# Я, как игрок, могу сделать несколько ставок на разные числа и получить выигрыш по тем, которые выиграли

import unittest

from casino.casino import Player, Game


class TestThree(unittest.TestCase):
    def test_player_can_lose_if_he_makes_the_wrong_bet(self):
        player_Alex = Player()
        player_Bob = Player()
        game = Game()
        game.add_player(player_Alex)
        game.add_player(player_Bob)
        player_Alex.buy_chips(300)
        player_Bob.buy_chips(400)

        player_Alex.bet(200, 6)
        player_Alex.bet(100, 5)
        player_Bob.bet(300, 5)
        player_Bob.bet(100, 4)
        game.play(predefined=[4])

        self.assertGreater(player_Bob.get_chips(), 0, "Bob should win")
        self.assertEqual(player_Alex.get_chips(), 0, "Alex should lose")

    def test_player_can_win_six_bets(self):
        player_Alex = Player()
        game = Game()
        game.add_player(player_Alex)
        chips_to_buy = 600
        player_Alex.buy_chips(chips_to_buy)

        for i in range(1, 7):
            player_Alex.bet(100, i)
        game.play(predefined=[4])

        self.assertGreaterEqual(player_Alex.get_chips(), chips_to_buy)

    def test_casino_receives_the_chips_that_the_player_lost(self):
        player_Alex = Player()
        game = Game()
        game.add_player(player_Alex)
        chips_to_buy = 600
        player_Alex.buy_chips(chips_to_buy)

        player_Alex.bet(600, 3)
        game.play(predefined=[4])

        self.assertEqual(game.get_casino_win(), chips_to_buy)

    def test_player_can_make_several_bets_on_different_numbers_and_win_on_those_that_won(self):
        player_Alex = Player()
        game = Game()
        game.add_player(player_Alex)
        chips_to_buy = 600
        player_Alex.buy_chips(chips_to_buy)

        player_Alex.bet(100, 1)
        player_Alex.bet(500, 4)
        game.play(predefined=[1, 4])

        self.assertGreaterEqual(player_Alex.get_chips(), chips_to_buy)

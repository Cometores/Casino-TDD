# Упражнение 4. Несколько кубиков
# Я, как крупье, могу сделать игру с двумя кубиками
# Я, как игрок, могу делать ставки на числа от 2 до 12
# Я, как казино, определяю выигрышный коэффициент по вероятности выпадения того или иного номера

import unittest
from casino.casino import Player, Game


class TestThree(unittest.TestCase):
    def test_player_can_play_two_dice_game(self):
        player_Alex = Player()
        game = Game("twodice")
        game.add_player(player_Alex)
        chips_to_buy = 600
        player_Alex.buy_chips(chips_to_buy)

        player_Alex.bet(100, 12)
        player_Alex.bet(500, 2)
        game.play_twodice(predefined=[12])

        self.assertGreaterEqual(player_Alex.get_chips(), 1200)

    def test_player_can_bet_on_numbers_from_2_to_12(self):
        player_Alex = Player()
        game = Game("twodice")
        game.add_player(player_Alex)
        chips_to_buy = 1200
        player_Alex.buy_chips(chips_to_buy)

        for i in range(2, 13):
            player_Alex.bet(100, i)

        with self.assertRaises(Exception):
            player_Alex.bet(100, 1)

        with self.assertRaises(Exception):
            player_Alex.bet(100, 13)

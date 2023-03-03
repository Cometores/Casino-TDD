# Упражнение 1. Создание нового домена с нуля Игрок и игра "Кости"
# Я, как игрок, могу войти в игру
# Я, как игрок, могу выйти из игры
# Я, как игрок, не могу выйти из игры, если я в нее не входил
# Я, как игрок, могу играть только в одну игру одновременно
# Я, как игрок, не могу зайти в одну игру дважды
# Я, как игра, не позволяю войти более чем 6 игрокам

import unittest

from casino.casino import Player, Game


class TestOne(unittest.TestCase):
    def test_player_can_enter_the_game(self):
        player = Player()
        game = Game("onedice")

        game.add_player(player)

        assert player in game.get_active_players()
        assert player.in_game

    def test_player_can_exit_the_game(self):
        player = Player()
        game = Game("onedice")

        game.add_player(player)
        game.remove_player(player)

        assert player not in game.get_active_players()
        assert not player.in_game

    def test_player_can_play_only_one_game(self):
        player = Player()
        game1 = Game("onedice")
        game2 = Game("onedice")

        game1.add_player(player)

        self.assertRaises(Exception, game2.add_player, player)

    def test_players_can_play_different_games(self):
        player2 = Player()
        player1 = Player()
        game1 = Game("onedice")
        game2 = Game("onedice")

        game1.add_player(player1)
        game2.add_player(player2)

        assert player1 in game1.get_active_players()
        assert player2 not in game1.get_active_players()

        assert player2 in game2.get_active_players()
        assert player1 not in game2.get_active_players()

    def test_game_can_only_have_six_players(self):
        game = Game("onedice")

        for i in range(6):
            game.add_player(Player())

        with self.assertRaises(Exception):
            game.add_player(Player())

    @unittest.skip
    def test_player_cannot_enter_game_twice(self):
        pass

    def test_player_cannot_leave_the_game_he_was_not_playing(self):
        player = Player()
        game = Game("onedice")

        with self.assertRaises(Exception):
            game.remove_player(player)

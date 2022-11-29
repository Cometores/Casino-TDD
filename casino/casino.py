import random


class Player:
    def __init__(self):
        self.bets_list: list[int] = [0] * 6
        self.bets_twodice_list: list[int] = [0] * 11
        self.in_game: bool = False
        self.__chips: int = 0

    def buy_chips(self, chips_to_buy: int):
        """
        Player buys any number of chips
        :param chips_to_buy: any Integer > 0
        :return:
        """
        # TODO: Check if chips_to_buy > 0
        self.__chips = chips_to_buy

    def bet(self, chips_to_bet: int, bet_number: int):
        """
        Player makes a bet in normal 1-dice game.
        :param chips_to_bet: int % 5
        :param bet_number: number from 1 to 6
        :return: void
        """
        # TODO: Bug chips_to_bet=0 -> bets_list[-1] = bets_list[5]
        if chips_to_bet > self.__chips or chips_to_bet % 5:
            raise Exception
        else:
            self.__chips -= chips_to_bet
            self.bets_list[bet_number - 1] += chips_to_bet

    def bet_two_dice(self, chips_to_bet: int, bet_number: int):
        """
        Player makes a bet in 2-dice game
        :param chips_to_bet: chips_to_bet: int % 5
        :param bet_number: bet_number: number from 2 to 12
        :return: void
        """
        if chips_to_bet > self.__chips or chips_to_bet % 5 or \
                bet_number < 2 or bet_number > 12:
            raise Exception
        else:
            self.__chips -= chips_to_bet
            self.bets_twodice_list[bet_number - 2] += chips_to_bet

    def get_bet(self, bet_number: int):
        """
        Get amount of chips for concrete betting number
        :param bet_number: betting number
        :return: void
        """
        return self.bets_list[bet_number - 1]

    def get_chips(self):  return self.__chips

    def set_chips(self, chips: int): self.__chips += chips


class Game:
    def __init__(self):
        self.__casino_win: int = 0
        self.players_list: list[Player] = []
        # self.coefficients: list[float] = [0] * 11

    def add_player(self, player: Player):
        """
        Adds player to the game if player wasn't already in a game
        :param player: Player
        :return: void
        """
        if player not in self.players_list and not player.in_game \
                and len(self.players_list) < 6:
            self.players_list.append(player)
            player.in_game = True
        else:
            raise Exception()

    def remove_player(self, player: Player):
        """
        Removes player from the game
        :param player: Player
        :return:  void
        """
        self.players_list.remove(player)
        player.in_game = False

    def play(self, predefined: list[int] = None):
        """
        Rolling a dice for normal 1-dice game -> 1-6
        and changing the components
        :param predefined: Predefine the result of rolling dice as list[int]
        :return: void
        """
        # self.calculate_the_coefficients()
        win_number = predefined if predefined else [random.randint(1, 6)]
        for player in self.players_list:
            for i in range(len(player.bets_list)):
                if i + 1 in win_number:
                    player.set_chips(player.bets_list[i] * 6)
                else:
                    self.__casino_win += player.bets_list[i]
                player.bets_list[i] = 0

    def play_twodice(self, predefined: list[int] = None):
        """
        Rolling a dices for 2-dice game -> 2-12
        and changing the components
        :param predefined: Predefine the result of rolling dices as list[int]
        :return: void
        """
        win_number = predefined if predefined else [random.randint(2, 12)]
        for player in self.players_list:
            for i in range(len(player.bets_twodice_list)):
                if i + 2 in win_number:
                    player.set_chips(player.bets_twodice_list[i] * self.calculate_the_coefficients())
                else:
                    self.__casino_win += player.bets_twodice_list[i]
                player.bets_twodice_list[i] = 0

    def calculate_the_coefficients(self): return 12

    def get_active_players(self): return self.players_list

    def get_casino_win(self): return self.__casino_win

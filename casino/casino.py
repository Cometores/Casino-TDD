import random


class Player:
    def __init__(self):
        self.bets_onedice_list: list[int] = [0] * 6
        self.bets_twodice_list: list[int] = [0] * 11
        self.in_game: bool = False
        self.game_type: str = ""
        self.__chips: int = 0

    def buy_chips(self, chips_to_buy: int):
        if chips_to_buy < 0:
            raise Exception
        self.__chips = chips_to_buy

    def bet(self, chips_to_bet: int, bet_number: int):
        if not self.in_game or chips_to_bet > self.__chips or chips_to_bet % 5:
            raise Exception

        if self.game_type == "onedice":
            self.bet_one_dice(chips_to_bet, bet_number)
        elif self.game_type == "twodice":
            self.bet_two_dice(chips_to_bet, bet_number)

    def bet_one_dice(self, chips_to_bet: int, bet_number: int):
        if bet_number > 6 or 1 > bet_number:
            raise Exception
        self.__chips -= chips_to_bet
        self.bets_onedice_list[bet_number - 1] += chips_to_bet

    def bet_two_dice(self, chips_to_bet: int, bet_number: int):
        if bet_number > 12 or bet_number < 2:
            raise Exception
        self.__chips -= chips_to_bet
        self.bets_twodice_list[bet_number - 2] += chips_to_bet

    def get_bet(self, bet_number: int):
        if self.game_type == "onedice" and 6 >= bet_number >= 1:
            return self.bets_onedice_list[bet_number - 1]
        elif self.game_type == "twodice" and 12 >= bet_number >= 2:
            return self.bets_twodice_list[bet_number - 1]
        raise Exception

    def get_chips(self):
        return self.__chips

    def set_chips(self, chips: int):
        self.__chips += chips


class Game:
    def __init__(self, game_type: str):
        self.__casino_win: int = 0
        self.players_list: list[Player] = []
        self.game_type: str = game_type
        # self.coefficients: list[float] = [0] * 11

    def add_player(self, player: Player):
        if player not in self.players_list and not player.in_game \
                and len(self.players_list) < 6:
            self.players_list.append(player)
            player.in_game = True
            player.game_type = self.game_type
        else:
            raise Exception()

    def remove_player(self, player: Player):
        self.players_list.remove(player)
        player.in_game = False
        player.in_game = ""

    def play(self, predefined: list[int] = None):
        if self.game_type == "onedice":
            self.play_one_dice(predefined)
        elif self.game_type == "twodice":
            self.play_twodice(predefined)

    def play_one_dice(self, predefined: list[int] = None):
        # self.calculate_the_coefficients()
        win_number = predefined if predefined else [random.randint(1, 6)]
        for player in self.players_list:
            for i in range(len(player.bets_onedice_list)):
                if i + 1 in win_number:
                    player.set_chips(player.bets_onedice_list[i] * 6)
                else:
                    self.__casino_win += player.bets_onedice_list[i]
                player.bets_onedice_list[i] = 0

    def play_twodice(self, predefined: list[int] = None):
        win_number = predefined if predefined else [random.randint(2, 12)]
        for player in self.players_list:
            for i in range(len(player.bets_twodice_list)):
                if i + 2 in win_number:
                    player.set_chips(player.bets_twodice_list[i] * self.calculate_the_coefficients())
                else:
                    self.__casino_win += player.bets_twodice_list[i]
                player.bets_twodice_list[i] = 0

    def calculate_the_coefficients(self):
        return 12

    def get_active_players(self):
        return self.players_list

    def get_casino_win(self):
        return self.__casino_win

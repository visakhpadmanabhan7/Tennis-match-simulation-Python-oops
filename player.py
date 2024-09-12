from tennis_constant import TennisConstants


class Player():
    def __init__(self,player_name):
        self.player_name=player_name
        self.player_point=TennisConstants.SCORE_LOVE
        self.player_status=TennisConstants.MATCH_START

    def get_player_name(self):
        return self.player_name

    def get_player_point(self):
        return self.player_point

    def update_player_point(self,is_deuce):
        match self.get_player_point():
            case TennisConstants.SCORE_LOVE:
                self.player_point=TennisConstants.SCORE_15
            case TennisConstants.SCORE_15:
                self.player_point = TennisConstants.SCORE_30
            case TennisConstants.SCORE_30:
                self.player_point = TennisConstants.SCORE_40
            case TennisConstants.SCORE_40 :
                if is_deuce:
                    self.player_point = TennisConstants.SCORE_ADVANTAGE
                else:
                    self.player_point=TennisConstants.WON

            case TennisConstants.SCORE_DUECE:
                if is_deuce:
                    self.player_point=TennisConstants.SCORE_40
                else:
                    self.player_point=TennisConstants.SCORE_ADVANTAGE
            case TennisConstants.SCORE_ADVANTAGE:
                if is_deuce:
                    self.player_point=TennisConstants.SCORE_DUECE
                else:
                    self.player_point=TennisConstants.WON
    def set_player_point(self):
        self.player_point=TennisConstants.SCORE_40

    def set_player_status(self,status):
        self.player_status=status

    def get_player_status(self):
        return self.player_status









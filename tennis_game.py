from game import Game
from tennis_constant import TennisConstants

class TennisGame(Game) :
    def __init__(self,player1,player2,input_test):
        self.player1=player1
        self.player2=player2
        self.match_status=TennisConstants.MATCH_START
        self.input_test=input_test
        self.duece_flag=False

    def print_current_score(self):
        print(f"===>>>>Score for {self.player1.get_player_name()} is {self.player1.get_player_point()}")
        print(f"===>>>>Score for {self.player2.get_player_name()} is {self.player2.get_player_point()}")
        print(f"-----------")

    def display_score(self):
        player1_score=self.player1.get_player_point()
        player2_score=self.player2.get_player_point()
        print(f"Score for {self.player1.get_player_name()} is {player1_score}")
        print(f"Score for {self.player2.get_player_name()} is {player2_score}")


    def check_deuce(self):
        if((self.player1.get_player_point()==self.player2.get_player_point()==TennisConstants.SCORE_40)):
            print(TennisConstants.SCORE_DUECE.value)
            print("----------")

            return True

    def match_result(self):
        if (
                self.player1.get_player_point() == TennisConstants.WON):
            return self.player1
        if (
                self.player2.get_player_point() == TennisConstants.WON):
            return self.player2
        else:
            return False

    def start_match(self):
        for i in range(0,len(self.input_test)):
            self.print_current_score()

            self.duece_flag=self.check_deuce()

            print(f"Service {i+1}")
            print(f"{self.input_test[i].get_player_name()} won the point")

            if self.input_test[i].get_player_name()==self.player2.get_player_name():
                if (self.player1.get_player_point() == TennisConstants.SCORE_ADVANTAGE):
                    self.player1.set_player_point()
                    continue

                self.player2.update_player_point(is_deuce=self.duece_flag)


            if self.input_test[i].get_player_name()==self.player1.get_player_name():
                if (self.player2.get_player_point() == TennisConstants.SCORE_ADVANTAGE):
                    self.player2.set_player_point()
                    continue

                self.player1.update_player_point(is_deuce=self.duece_flag)

            if (self.match_result()):
                break


            # if(self.check_match_status()==TennisConstants.FINISHED):
            #     print("MATCH FINISH")

        self.print_current_score()
        match_result=self.match_result()
        if (match_result):
            print(f"Match Finished,{match_result.get_player_name()} won")
        print("xxxxxxxxxxxxxxxxxxxxxx")







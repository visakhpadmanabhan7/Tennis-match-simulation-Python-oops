class Game:
    def __init__(self,game):
        self.game=game
        self.curr_score=0
    def set_score(self,score):
        self.curr_score=score
    def get_score(self):
        return self.curr_score
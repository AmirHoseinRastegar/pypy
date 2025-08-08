class Score_calculator:
    def __init__(self, starting_score=100):
        self.score= starting_score
        
    def decrement_score(self,interval=10):
        self.score -= interval
        self.score = max(self.score,0)  
    
    def show_score(self):
       return self.score       
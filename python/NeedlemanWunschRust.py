from lib import needleman_wunsch_rust as nW 

class NeedlemanWunschRust:
    
    def __init__(self):
        self
    

    def getScore(self, seq1, seq2):
        score = nW.get_score(seq1, seq2 )
        return score
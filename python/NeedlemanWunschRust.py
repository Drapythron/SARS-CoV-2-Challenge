from lib import needleman_wunsch_rust as nW 

class NeedlemanWunschRust:
    alignment1 = ""
    alignment2 = ""
    
    def __init__(self):
        self
    
    def newEntry(self, seq1, seq2): 
        x = nW.get_alignment(seq1, seq2)
        self.alignment1 = x[0]
        self.alignment2 = x[1]

    def getScore(self):
        score = nW.get_score(self.alignment1, self.alignment2)
        return score
    
    def getAlignment(self):
        return self.alignment1, self.alignment2

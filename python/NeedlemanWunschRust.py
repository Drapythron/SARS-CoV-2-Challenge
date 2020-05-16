from lib import needleman_wunsch_rust as nW 

class NeedlemanWunschRust:
    
    def __init__(self):
        self
    

    def getScore(self, seq1, seq2):
        score = nW.get_score(seq1, seq2)
        print(score)

        #CREMOS LA NUEVA PUNTUACIÓN DE 0 A 100

        """maxim = max(len(seq1), len(seq2))

        score += maxim

        newScore = (score / (maxim * 2)) * 100

        newScore = 100 - newScore

        return newScore"""
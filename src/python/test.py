import unittest
import sys
import NeedlemanWunsch
import NeedlemanWunschRust

class NeedlemanWunsch_test(unittest.TestCase):

    def test_getScore(self):
        nW = NeedlemanWunsch.NeedlemanWunsch()
        nW.newEntry("AACGT", "GTACG")
        score = nW.getScore()
        self.assertEqual(score, 50)
    
    def test_otherNucleotide(self):
        nW = NeedlemanWunsch.NeedlemanWunsch()
        nW.newEntry("NWCGT", "GTACG")
        score = nW.getScore()
        self.assertEqual(score, 50)

class NeedlemanWunschRust_test(unittest.TestCase):
    def test_getScore(self):
        nW = NeedlemanWunschRust.NeedlemanWunschRust()
        score = nW.getScore("AACGT", "GTACG")
        self.assertEqual(score, 50)
    
    def test_otherNucleotide(self):
        nW = NeedlemanWunschRust.NeedlemanWunschRust()
        score = nW.getScore("NWCGT", "GTACG")
        self.assertEqual(score, 50)


if __name__ == "__main__":
    unittest.main()
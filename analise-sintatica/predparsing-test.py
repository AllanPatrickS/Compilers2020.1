import unittest
from predparsing import Grammar

class TestPredParsing(unittest.TestCase):

    def test_ex430(self):
        p = {"E" : [("T", "E'")],
             "E'" : [("+", "T", "E'"), ("epsilon",)],
             "T" : [("F", "T'")],
             "T'" : [("*", "F", "T'"), ("epsilon",)],
             "F" : [("(", "E", ")"), ("id",)]}
        g = Grammar("E", p, ["E", "E'", "T", "T'", "F"], ["+", "*", "(", ")", "id"])
        g.compute_first()
        g.compute_follow()
        g.compute_pred_parsing_tab()
        self.assertEqual(g.first_tab, {'E': {'id', '('}, "E'": {'+', 'epsilon'}, 'T': {'id', '('}, "T'": {'*', 'epsilon'}, 'F': {'id', '('}, '+': {'+'}, '*': {'*'}, '(': {'('}, ')': {')'}, 'id': {'id'}})
        self.assertEqual(g.follow_tab, {'E': {')', '$'}, "E'": {')', '$'}, 'T': {'+', ')', '$'}, "T'": {'+', '$', ')'}, 'F': {'+', '$', ')', '*'}})
        self.assertEqual(g.pred_parsing_tab, {'E': {'+': [], '*': [], '(': ["E -> TE'"], ')': [], 'id': ["E -> TE'"], '$': []}, "E'": {'+': ["E' -> +TE'"], '*': [], '(': [], ')': ["E' -> epsilon"], 'id': [], '$': ["E' -> epsilon"]}, 'T': {'+': [], '*': [], '(': ["T -> FT'"], ')': [], 'id': ["T -> FT'"], '$': []}, "T'": {'+': ["T' -> epsilon"], '*': ["T' -> *FT'"], '(': [], ')': ["T' -> epsilon"], 'id': [], '$': ["T' -> epsilon"]}, 'F': {'+': [], '*': [], '(': ['F -> (E)'], ')': [], 'id': ['F -> id'], '$': []}})

    def test_ex433(self):
        p = {"S" : [("i", "E", "t", "S", "S'"), ("a", )],
             "S'" : [("e", "S"), ("epsilon",)],
             "E" : [("b",)]}
        g = Grammar("S", p, ["S", "S'", "E"], ["a", "b", "e", "i", "t"])
        g.compute_first()
        g.compute_follow()
        g.compute_pred_parsing_tab()
        self.assertEqual(g.first_tab, {'S': {'a', 'i'}, "S'": {'e', 'epsilon'}, 'E': {'b'}, 'a': {'a'}, 'b': {'b'}, 'e': {'e'}, 'i': {'i'}, 't': {'t'}})
        self.assertEqual(g.follow_tab, {'S': {'e', '$'}, "S'": {'e', '$'}, 'E': {'t'}})
        self.assertEqual(g.pred_parsing_tab, {'S': {'a': ['S -> a'], 'b': [], 'e': [], 'i': ["S -> iEtSS'"], 't': [], '$': []}, "S'": {'a': [], 'b': [], 'e': ["S' -> eS", "S' -> epsilon"], 'i': [], 't': [], '$': ["S' -> epsilon"]}, 'E': {'a': [], 'b': ['E -> b'], 'e': [], 'i': [], 't': [], '$': []}})
        
if __name__ == '__main__':
    unittest.main()

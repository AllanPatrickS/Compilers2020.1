import unittest
import tatsu
from random import randrange, choice
from list_comp import ListCompSemantics


class TestListComp(unittest.TestCase):
    def setUp(self):
        fh = open('list_comp.ebnf')
        grammar = fh.read()
        fh.close()
        self.parser = tatsu.compile(grammar)

    def test_list_number(self):
        nl = []
        for i in range(100):
            nl.append(randrange(100))
        l =  '[x in {num_list} | (not (x > 10)) and (not (x == 10)) and (x > 2)]'.format(num_list = nl)
        ast = self.parser.parse(l, semantics=ListCompSemantics())
        r = list(filter(lambda _ : _ < 10 and _ > 2, nl))
        self.assertEqual(list(ast),r)

    def test_exp_list(self):
        nl = '['
        nl_i = []
        for i in range(100):
            op = choice(['+', '*', '/', '-'])
            oper1 = randrange(100)
            oper2 = randrange(100)
            if op != '/' and oper2 != 0:
                nl = nl + str(oper1) + op + str(oper2) + ','
                if op == '+':
                    nl_i.append(oper1 + oper2)
                elif op == '*':
                    nl_i.append(oper1 * oper2)
                elif op == '-':
                    nl_i.append(oper1 - oper2)
                else:
                    nl_i.append(oper1 / oper2)                    
                    
        nl = nl[:len(nl) - 1] + ']'
        l =  '[x in {num_list!s} | (not (x > 10)) and (not (x == 10)) and (x > 2)]'.format(num_list = nl)
        ast = self.parser.parse(l, semantics=ListCompSemantics())
        r = list(filter(lambda _ : _ < 10 and _ > 2, nl_i))
        self.assertEqual(list(ast),r)
        
if __name__ == '__main__':
    unittest.main()

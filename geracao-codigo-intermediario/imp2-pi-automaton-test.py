import unittest
import tatsu
from impiler import Impiler
from pi import run

class TestPiAut(unittest.TestCase):
    def setUp(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        self.parser = tatsu.compile(imp_grammar)

    def __test_pi_aut(self, file_name, state, text):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        pi_ast = self.parser.parse(source, semantics=Impiler())
        (trace, step, out, dt) = run(pi_ast, color=False)
        self.assertTrue(text in str(trace[state]))

    def test_exp(self):
        '''
        Ao executar o programa Imp em exp-test0.imp2, em qual estado o programa 
        está na sua forma pos-fixada na pilha de controle?
        '''
        control = "cnt : ['#BLKCMD', '#PRINT', '#LT', 1, '#MUL', 4, '#DIV', 3, 3]"
        state = 4
        assert(type(control) == str and type(state) == int)
        self.__test_pi_aut('exp-test0.imp2', state, control)
        
if __name__ == '__main__':
    unittest.main()

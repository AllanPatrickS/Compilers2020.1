import unittest
import tatsu
from impiler import Impiler

class TestImpToPiIR(unittest.TestCase):
    def setUp(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        self.parser = tatsu.compile(imp_grammar)

    def __test_parse(self, file_name, ast):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        pi_ast = self.parser.parse(source, semantics=Impiler())
        self.assertEqual(str(pi_ast), ast)

    def test_cmd_parse0(self):
        '''
        Escreva a representação em Pi IR do programa Imp em examples/cmd-test0.imp2.
        '''
        pi_ast = "Blk(Bind(Id(x), Ref(10)), Blk(Bind(Id(y), Ref(1)), CSeq(Loop(Gt(Id(x), 0), Blk(CSeq(Assign(Id(y), Mul(Id(y), Id(x))), Assign(Id(x), Sub(Id(x), 1))))), Print(Id(y)))))"
        self.__test_parse('examples/cmd-test0.imp2', pi_ast)

    def test_cmd_parse1(self):
        '''
        Escreva a representação em Pi IR do programa Imp em examples/cmd-test1.imp2.
        '''
        pi_ast = "Blk(DSeq(Bind(Id(x), Ref(1)), Bind(Id(y), Ref(0))), Blk(Bind(Id(z), Ref(0)), CSeq(CSeq(CSeq(CSeq(Assign(Id(x), 0), Assign(Id(y), 1)), Assign(Id(z), 3)), Cond(Lt(Id(x), 2), Blk(Assign(Id(z), 3)), Nop())), Print(Id(z)))))"
        self.__test_parse('examples/cmd-test1.imp2', pi_ast)
        
if __name__ == '__main__':
    unittest.main()

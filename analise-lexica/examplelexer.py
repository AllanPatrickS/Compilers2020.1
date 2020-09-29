# ------------------------------------------------------------
# Dragon book - Exercise 3.5.1 
# ------------------------------------------------------------
import ply.lex as lex

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE'
}

# List of token names.   This is always required
tokens = [
    'LT',
    'LE',
    'EQ',
    'NE',
    'GE',
    'GT',
    'ID',
    'NUMBER',
    'STRING',
    'RELOP'
] + list(reserved.values())

# A string containing ignored characters (spaces, tabs and newline)
t_ignore  = ' \t\n'

def t_LE(t):
    r'<='
    t.type = 'RELOP'
    t.value = 'LE'
    return t

def t_NE(t):
    r'!='
    t.type = 'RELOP'
    t.value = 'NE'
    return t

def t_GE(t):
    r'>='
    t.type = 'RELOP'
    t.value = 'GE'
    return t

def t_LT(t):
    r'<'
    t.type = 'RELOP'
    t.value = 'LT'
    return t

def t_GT(t):
    r'>'
    t.type = 'RELOP'
    t.value = 'GT'
    return t

def t_EQ(t):
    r'=='
    t.type = 'RELOP'
    t.value = 'EQ'
    return t

def t_ID(t):
    r'[\_]*[a-zA-Z][a-zA-Z0-9\_]*'
    t.type = reserved.get(t.value,'ID') # Check for reserved words
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'[\"][a-zA-Z0-9\_\"\\]*[\"]'
    t.type = 'STRING'
    t.value = str(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

class Ex351Lexer:
    data = None
    lexer = None

    def __init__(self):
        self.lexer = lex.lex()

    def setData(self, data):
        self.data = data
        self.lexer.input(data)
        
    def tokenize(self):
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            tokens.append(tok)
        return tokens

if __name__ == '__main__':
    lex = Ex351Lexer()
    lex.setData("if x then 3 <= 4 else 20 >= 1")
    print(lex.tokenize())

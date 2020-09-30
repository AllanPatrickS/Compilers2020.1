# ------------------------------------------------------------
# Processing a log file
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'TIMESTAMP',
    'PROC',
    'MESSAGE'
]


def t_TIMESTAMP(t):
    r'\d{2}\:\d{2}\:\d{2}\.\d{6}\s\-\d{4}'
    return t


def t_PROC(t):
    r'\t[\ a-zA-z\.\-]+\t'
    t.value = t.value[1:len(t.value) - 1]
    return t


def t_MESSAGE(t):
    r'[^\t]*\n'
    t.value = t.value[:len(t.value) - 1]
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


class LogProcLexer:
    data = None
    lexer = None

    def __init__(self):
        fh = open("log", 'r')
        self.data = fh.read()
        fh.close()
        self.lexer = lex.lex()
        self.lexer.input(self.data)

    def collect_messages(self):
        tokens = []
        while True:
            timestamp = self.lexer.token()
            proc = self.lexer.token()
            message = self.lexer.token()
            if not timestamp or not proc or not message :
                break
            if proc.value == "kernel" :
                tokens.append(message)
        return tokens


if __name__ == '__main__':
    print(LogProcLexer().collect_messages())

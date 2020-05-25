
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file. nvl(a, b)
# -----------------------------------------------------------------------------

tokens = (
    'NAME','NUMBER',
    'COMMA', 'EQUALS',
    'LPAREN','RPAREN',
    'NVL','NULL'
)

# Tokens

t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA  = r'\,'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NVL(t):
    r'NVL'
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_NULL(t):
    r'null|NULL|None'
    t.value = None
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()



data = "NVL(12,102)"

lexer.input(data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)


def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_decode(t):
    '''expression : NUMBER COMMA NUMBER
                  | NULL COMMA NUMBER
    '''
    t[0] = t[3] if t[1] is None else t[1]

def p_expression_NVL(t):
    'expression : NVL expression'
    t[0] = t[2]

def p_expression_NULL(t):
    'expression : NULL'
    t[0] = t[1]



import ply.yacc as yacc
# Build the parser
parser = yacc.yacc(debug=1)

try:
    s = data
    result = parser.parse(s)
    print(result)
except EOFError:
    result = parser.parse(s)
    print(result)

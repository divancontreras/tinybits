# -----------------------------------------------------------------------------
# TinyBit_Lex.py
#
# SYNTAX CHECKER FOR TINY BITS all in one file.
# -----------------------------------------------------------------------------


import ply.lex as lex


tokens = (
    

    'START',
    'END',
    'SETOUT',
    'GETIN',
    'DO',
    'LOOP',
    'EQUALS',
    'PROCCES',
    'IDENTIFIER',
    'NUM_INT',
    'NUM_FLOAT',
    'LPAREN',
    'RPAREN',
    'THEN',
    'COMMA',
    'LSQBRACK',
    'RSQBRACK',
    'MAIN',
    'COLON',
    'PLUS',
    'EXP',
    'MINUS',
    'MUL',
    'DIV',
    'MOD',
    'BIT_AND',
    'BIT_OR',
    'BIT_NEG',
    'DOUBLE_PLUS',
    'DOUBLE_MINUS',
    'TRUE',
    'FALSE',
    'EQ',
    'NEQ',
    'GT',
    'GTE',
    'LT',
    'LTE',
    'ARROW_LTR',
    'ARROW_RTL',
    'IF',
    'ELSE',
    'IN',
    'FOR',
    'WHILE',
    'AND',
    'OR',
    'NOT'


    )

# Tokens

t_COMMA = ','
t_PLUS = r'\+'
t_EXP = r'\*\*'
t_MINUS = '-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = '%'
t_EQUALS = '='
t_ignore_WS = r'\s+'
t_COLON = ':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQBRACK = r'\['
t_RSQBRACK = r'\]'
t_DOUBLE_PLUS = r'\+\+'
t_DOUBLE_MINUS = '--'
t_EQ = '=='
t_NEQ = '!='
t_BIT_AND = r'\&\&'
t_BIT_OR = r'\|\|'
t_BIT_NEG = r'\!'
t_GT = '>'
t_GTE = '>='
t_LT = '<'
t_LTE = '<='
t_ARROW_LTR = '->'
t_ARROW_RTL = '<-'
t_ignore_COMMENTS = r'//.+'




def t_SETOUT(t):
    r'setOut'
    return t
    
def t_GETIN(t):
    r'getIn'
    return t

def t_TRUE(t):
    'True'
    return t


def t_FALSE(t):
    'False'
    return t

def t_THEN(t):
    'Then'
    return t

def t_IDENTIFIER(t):
    r'\w+(_\d\w)*'
    return t

def t_NUM_FLOAT(t):
    r'\d*\.\d+'
    return t

def t_PROCCES(t):
    r'Procces'
    return t

def t_MAIN(t):
    r'Main'
    return t    

def t_END(t):
    r'End'
    return t

def t_START(t):
    r'Start'
    return t

def t_NUM_INT(t):
    r'\d+'
    return t

def t_LOOP(t):
    r'Loop'
    return t

def t_DO(t):
    r'Do'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_error(t):
    print (("Error Lexico: " + str(t.value[0])))
    t.lexer.skip(1)
    
# Build the lexer

lexer = lex.lex()
"""
while True:
    data = input(">>")

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
"""
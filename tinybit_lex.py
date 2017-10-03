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
    'TO',
    'GETIN',
    'ELSE',
    'IF',
    'THEN',
    'DO',
    'PROCESS',
    'CALL',
    'FLOAT',
    'LOOP',
    'INT',
    'WHILE',
    'FOR',
    'ID',
    'NUMBER',
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'COLON',
    'QUOTES',
    'MAIN',
    'ENDL'

    )

# Tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_MINUSMINUS = r'\-\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'\='
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_QUOTES = r'\"'
t_COLON = r'\:'

# Ignored characters
t_ignore = " \t"

def t_SETOUT(t):
    r'setOut'
    return t

def t_START(t):
    r'START'
    return t


def t_GETIN(t):
    r'getIn'
    return t

def t_PROCESS(t):
    r'Process'
    return t

def t_MAIN(t):
    r'Main'
    return t

def t_ELSE(t):
    r'else'
    return t


def t_IF(t):
    r'if'
    return t

def t_THEN(t):
    r'then'
    return t

def t_LOOP(t):
    r'loop'
    return t

def t_DO(t):
    r'Do'
    return t

def t_ENDL(t):
    r'endl'
    return t

def t_END(t):
    r'END'
    return t

def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_WHILE(t):
    r'while'
    return t


def t_FOR(t):
    r'for'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#expresion regular para reconocer los identificadores

def t_ID(t):
    r'\w+(_\d\w)*'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_LESSEQUAL(t):
    r'<='
    return t


def t_LESS(t):
    r'<'
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_GREATER(t):
    r'>'
    return t

def t_DEQUAL(t):
    r'=='
    return t

def t_CALL(t):
    r'CallProcess'
    return t

def t_TO(t):
    r'To'
    return t


def t_DISTINT(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print (("Error Lexico: " + str(t.value[0])))
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

# data = input(">>")

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)

# -----------------------------------------------------------------------------
# parseronfile.py
#
# SYNTAX CHECKER WITH GRAMMAR FOR "HOLA(, HOLA)* QUE TAL"-- all in one file.
# -----------------------------------------------------------------------------


tokens = (
    'HOLA','COMA',
    'QUE','TAL',
    )

# Tokens

t_HOLA    = r'HOLA'
t_QUE     = r'QUE'
t_TAL     = r'TAL'
t_COMA    = r'\,'

# Ignored characters
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

def p_error(t):
    print("INPUT RECHAZADO")

def p_ForS(t):
 """
    ForS : ForX QUE TAL
 """
def p_ForX(t):
    """   
       ForX : HOLA
            | ForX COMA HOLA
     """
 # BUild the parser
import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('>> ')  
    except EOFError:
        break
    parser.parse(s)

import ply.yacc as yacc
from tinybits_lex import tokens


VERBOSE = 1

def p_error(p):
    if VERBOSE:
        if p is not None:
            print ("Error en Sintaxis linea:" + str(p.lexer.lineno)+"  Error de Contexto " + str(p.value))
        else:
            print ("Error en Lexico linea: " + str(c_lexer.lexer.lineno))
    else:
        raise Exception('Syntax', 'error')


def p_program(p):
    'program : START program_start END'
    pass

def p_program_main(p):
    'program_start : statement_list main_declaration'
    pass   


def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    pass


def p_statement(p):
    '''
    statement : identifier
              | expression
              | if_statement
    '''
    pass


def p_main_declaration(p):
    'main_declaration : MAIN identifier COLON statement_list END'
    pass

def p_identifier(p):
    '''
    identifier : IDENTIFIER
    '''
    pass

def p_primitive(p):
    '''
    primitive : NUM_INT
              | NUM_FLOAT
              | boolean
    '''
    pass


def p_binary_op(p):
    '''
    expression : expression PLUS expression PLUS
            | expression MINUS expression MINUS
            | expression MUL expression MUL
            | expression DIV expression DIV
            | expression EXP expression EXP
            | expression MOD expression MOD
            | expression BIT_AND expression
            | expression BIT_OR expression

    '''
    pass
def p_boolean_operators(p):
    '''
    boolean : expression EQ expression
            | expression NEQ expression
            | expression GT expression
            | expression GTE expression
            | expression LT expression
            | expression LTE expression
            | expression AND expression
            | expression OR expression
    '''
    pass

def p_unary_operation(p):
    '''
    expression : MINUS expression MINUS
               | PLUS expression PLUS
               | BIT_NEG expression
               | NOT expression
    '''
    pass

def p_paren(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    pass

def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''
    pass

def p_assignable(p):
    '''
    assignable : primitive
               | expression
    '''
    pass

def p_comma_separated_expr(p):
    '''
    arguments : arguments COMMA expression
              | expression
              | 
    '''
    pass


def p_arrays(p):
    '''
    expression : LSQBRACK arguments RSQBRACK
    '''
    pass

def p_array_access(p):
    '''
    expression : identifier LSQBRACK expression RSQBRACK
    '''
    pass

def p_slice(p):
    '''
    expression : identifier LSQBRACK expression COLON expression RSQBRACK
               | identifier LSQBRACK COLON expression RSQBRACK
               | identifier LSQBRACK expression COLON RSQBRACK
               | identifier LSQBRACK COLON RSQBRACK
    '''
    pass


def p_array_access_assign(p):
    '''
    statement : identifier LSQBRACK expression RSQBRACK EQUALS expression 
    '''
    pass

def p_assign(p):
    '''
    expression : identifier EQUALS assignable
    '''
    pass

def p_ifstatement(p):
    '''
    if_statement : IF expression THEN statement_list END
    '''
    pass

def p_ifstatement_else(p):
    '''
    if_statement : IF expression THEN statement_list ELSE statement_list END
    '''
    pass

def p_ifstatement_else_if_else(p):
    '''
    if_statement : IF expression THEN statement_list ELSE if_statement
    '''
    pass

def p_in_expression(p):
    '''
    expression : expression IN expression
               | expression NOT IN expression
    '''
    pass

def p_SETOUT_statement(p):
    '''
    statement : SETOUT arguments
    '''
    pass

def p_GETIN_statement(p):
    '''
    statement : GETIN arguments
    '''
    pass


def p_increment_decrement_identifiers(p):
    '''
    expression : identifier DOUBLE_PLUS
               | identifier DOUBLE_MINUS
    '''
    pass

def p_expression(p):
    '''
    expression : primitive
               | identifier
    '''
    pass

def p_for_loop(p):
    '''
    statement : FOR identifier IN expression ARROW_LTR expression DO statement_list LOOP
              | FOR identifier IN expression ARROW_RTL expression DO statement_list LOOP
    '''
    pass

def p_for_in_loop(p):
    '''
    statement : FOR identifier IN expression DO statement_list LOOP
    '''
    pass

def p_while_loop(p):
    '''
    statement : WHILE expression DO statement_list LOOP
    '''
    pass


def p_procces_declaration(p):
    '''
    statement : PROCCES identifier COLON statement_list END
    '''
    pass


def p_procces_call(p):
    '''
    expression : PROCCES identifier ARROW_LTR START
    statement : PROCCES identifier ARROW_LTR START
    '''
    pass


import ply.yacc as yacc
parser = yacc.yacc(debug=True)

while True:
    try:
        input("OUTPUT:")
        s = open('codehw.txt', 'r').read()
    except EOFError:
        break
    parser.parse(s) 
from tinybit_lex import tokens

VERBOSE = 1

def p_error(p):
    #print str(dir(p))
    #print str(dir(c_lexer))
    if VERBOSE:
        if p is not None:
            print ("Error en Sintaxis linea:" + str(p.lexer.lineno)+"  Error de Contexto " + str(p.value))
        else:
            print ("Error en Lexico linea: " + str(c_lexer.lexer.lineno))
    else:
        raise Exception('Syntax', 'error')

def p_program(p):
    'program : START program_main END'
    pass

def p_force_main(p):
    'program_main : program_sequence main_declaration '
    pass

def p_main_declaration(p):
    'main_declaration : MAIN COLON statements_nont END'
    pass

def p_program_begin(p):
    """
    program_sequence : program_sequence
                    | statements_nont
                    | PROCESS_declaration
                    | call
    """
    pass   



def p_var_declaration(p):
    '''var_declaration : var_type ID
    | var_type ID COMMA ID
    | var_type ID EQUAL NUMBER
    | var_type ID EQUAL var
    '''
    pass


def p_var_type_INT(p):
    'var_type : INT'
    pass


def p_var_type_FLOAT(p):
    'var_type : FLOAT'
    pass


def p_var_declaration_array(p):
    """
    var_declaration : var_type ID dimensiones 
    """
    pass 


def p_var_dimensiones_array(p):
    """
    dimensiones : dimensiones LBRACKET expression RBRACKET
                | LBRACKET expression RBRACKET
    """
    pass 


def p_PROCESS_declaration(p):
    'PROCESS_declaration : PROCESS ID DO statements_nont END'
    pass


def p_statements_nont(p):
    """
    statements_nont : statements_nont statement
                    | statement
    """
    pass

def p_statement(p):
    '''statement : expression_nont
            | condition_nont
            | iteration_nont
            | var_declaration
            | call
    '''
    pass


def p_expression_simple(p):
    '''expression_nont : expression'''
    pass


def p_expression_SETOUT(p):
    '''expression_nont : SETOUT LPAREN QUOTES ID QUOTES RPAREN 
    | SETOUT LPAREN QUOTES ID QUOTES COMMA ENDL RPAREN 
    | SETOUT LPAREN var RPAREN
    | SETOUT LPAREN var COMMA ENDL RPAREN 
    | SETOUT LPAREN var COMMA var COMMA RPAREN 
    | SETOUT LPAREN var COMMA var COMMA ENDL RPAREN 
    '''
    pass


def p_expression_GETIN(p):
    '''expression_nont : GETIN LPAREN var RPAREN
    | GETIN LPAREN var COMMA var RPAREN
    '''
    pass


def p_expression_overload(p):
    '''expression_nont : ID PLUSPLUS
    | ID MINUSMINUS
    '''
    pass

def p_condition_if(p):
    'condition_nont : IF expression THEN statements_nont END'
    pass


def p_condition_if_else(p):
    'condition_nont : IF expression THEN statements_nont ELSE statements_nont END'
    pass


def p_iteration_while(p):
    'iteration_nont : WHILE expression DO statements_nont LOOP'
    pass


def p_iteration_for(p):
    'iteration_nont : FOR var TO var DO statements_nont LOOP'
    pass


def p_expression_equal(p):
    '''expression : var EQUAL expression'''
    pass


def p_var_ID(p):
    'var : ID'
    pass

def p_var_bracket(p):
    """
    var : var ID LBRACKET expression RBRACKET
    | ID vardimen
    """
    pass

def p_var_dimen(p):
    """
    vardimen : vardimen LBRACKET expression RBRACKET
    | LBRACKET expression RBRACKET
    """
    pass


def p_expression_2(p):
    'expression : simple_expression'
    pass


def p_simple_expression_1(p):
    'simple_expression : additive_expression checkop additive_expression'
    pass


def p_simple_expression_2(p):
    'simple_expression : additive_expression'
    pass


def p_checkop(p):
    '''checkop : LESS
        | LESSEQUAL
        | GREATER
        | GREATEREQUAL
        | DEQUAL
        | DISTINT
    '''
    pass


def p_additive_expression_1(p):
    """
    additive_expression : additive_expression addop term
                        | term
    """
    pass


def p_addop(p):
    '''addop : PLUS
    | MINUS
    '''
    pass

def p_factor(p):
    """
    factor : LPAREN expression RPAREN
           | var
           | NUMBER
    """
    pass


def p_call(p):
    'call : CALL LPAREN ID RPAREN'
    pass


def p_term_mulop(p):
    """
    term : term mulop factor
        | factor
    """
    pass

def p_mulop(p):
    '''mulop :  TIMES
                | DIVIDE
    '''
    pass


 # BUild the parser
import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = open('codehw.txt', 'r').read()
        input("OUTPUT:")
    except EOFError:
        break
    parser.parse(s) 

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
    'program : START program_sequence END'
    pass


def p_program_begin(p):
    'program_sequence : program_sequence declaration'
    pass   


def p_program_sequence(p):
    'program_sequence : declaration' 

    pass


def p_declaration(p):
    """declaration : var_declaration
    | procces_declaration
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
    'var_declaration : var_type ID LBRACKET NUMBER RBRACKET'
    pass


def p_procces_declaration(p):
    'procces_declaration : PROCCES ID COLON statements_nont END'
    pass


def p_statements_nont(p):
    'statements_nont : statements_nont statement'
    pass

def p_statements_empty(p):
    'statements_nont : empty'
    pass

def p_statement(p):
    '''statement : expression_nont
            | condition_nont
            | iteration_nont
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
    | PLUSPLUS ID
    | ID MINUSMINUS
    | MINUSMINUS ID
    '''
    pass

def p_condition_if(p):
    'condition_nont : IF expression THEN statement END'
    pass


def p_condition_if_else(p):
    'condition_nont : IF expression THEN statement ELSE statement END'
    pass


def p_iteration_while(p):
    'iteration_nont : WHILE expression DO statement LOOP'
    pass


def p_iteration_for(p):
    '''iteration_nont : FOR var COMMA expression COMMA expression DO statement LOOP
| FOR var COMMA expression COMMA var PLUSPLUS DO statement LOOP
| FOR var COMMA expression COMMA PLUSPLUS var DO statement LOOP
| FOR var COMMA expression COMMA var MINUSMINUS DO statement LOOP
| FOR var COMMA expression COMMA MINUSMINUS var DO statement LOOP
    '''
    pass


def p_expression_equal(p):
    '''expression : var EQUAL expression'''
    pass


def p_var_ID(p):
    'var : ID'
    pass


def p_var_bracket(p):
    'var : ID LBRACKET expression RBRACKET'
    pass


def p_expression_2(p):
    'expression : simple_expression'
    pass


def p_simple_expression_1(p):
    'simple_expression : additive_expression relop additive_expression'
    pass


def p_simple_expression_2(p):
    'simple_expression : additive_expression'
    pass


def p_relop(p):
    '''relop : LESS
        | LESSEQUAL
        | GREATER
        | GREATEREQUAL
        | DEQUAL
        | DISTINT
        | QUOTES
    '''
    pass


def p_additive_expression_1(p):
    'additive_expression : additive_expression addop term'
    pass


def p_additive_expression_2(p):
    'additive_expression : term'
    pass


def p_addop(p):
    '''addop : PLUS
    | MINUS
    '''
    pass

def p_factor_3(p):
    'factor : call'
    pass


def p_call(p):
    'call : PROCCES ID'
    pass


def p_term_1(p):
    'term : term mulop factor'
    pass


def p_term_2(p):
    'term : factor'
    pass


def p_mulop(p):
    '''mulop :  TIMES
                | DIVIDE
    '''
    pass


def p_factor_1(p):
    'factor : LPAREN expression RPAREN'
    pass


def p_factor_2(p):
    'factor : var'
    pass

def p_factor_4(p):
    'factor : NUMBER'
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
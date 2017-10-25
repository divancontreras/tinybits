from tinybit_lex import tokens
from intvar import *
from floatvar import *

VERBOSE = 1
vtable = {}
ints = []
floats = []
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

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

def p_error_repeat_var(p):
    print("Error, la variable \"" + str(p) + "\" está repetida")

def p_program(p):
    'program : START program_main END'
    pass

def p_force_main(p):
    'program_main : program_sequence main_declaration '
    #p[0] = p[1] + p[2]
    print(vtable)
    for var in ints:
        print("ID: " + var.getId() + " VALUE: " + str(var.getValue()))

    pass

def p_main_declaration(p):
    'main_declaration : MAIN COLON statements_nont END'
    pass

def p_program_begin(p):
    """
    program_sequence : program_sequence
                    | statements_nont
                    | PROCESS_declaration
    """
    pass   


def p_var_declare_novalue(p):
    'var_declaration : var_type ID'

def p_var_declaration(p):
    '''var_declaration : var_type ID COMMA ID
    | var_type ID EQUAL NUMBER
    | var_type ID EQUAL NUMBER_FLOAT    
    | var_type ID EQUAL var
    | var_type ID EQUAL simple_expression
    '''
    if p[2] in vtable:
        p_error_repeat_var(p[2])
        exit()
    else:
        vtable[p[2]] = p[1]
    if p[1] == 'INT':
        ints.append(Int(p[2],p[4]))
    elif p[1] == 'FLOAT':
        floats.append(Float(p[2],p[4]))
    
def p_var_type_INT(p):
    'var_type : INT'
    p[0] = "INT"
    pass


def p_var_type_FLOAT(p):
    'var_type : FLOAT'
    p[0] = "FLOAT"
    pass


def p_var_declaration_array(p):
    """
    var_declaration : var_type ID dimensiones 
    """
    if p[2] in vtable:
        p_error_repeat_var(p[2])
    else:
        vtable[p[2]] = p[1]

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
    '''expression_nont : var PLUSPLUS
    | var MINUSMINUS
    '''                       
    if p[2] == '++':
        p[1].setValue(p[1].getValue()+1)
    else:
        p[1].setValue(p[1].getValue()-1)

def p_condition_if(p):
    'condition_nont : IF expression THEN statements_nont END'
    pass


def p_condition_if_else(p):
    'condition_nont : IF expression THEN statements_nont ELSE statements_nont END'
    pass

def p_iteration_for(p):
    """
    iteration_nont : FOR expression ARROW expression DO statements_nont LOOP
    """
    pass

def p_iteration_while(p):
    'iteration_nont : WHILE expression DO statements_nont LOOP'
    pass


def p_expression_equal(p):
    '''expression : var EQUAL expression'''
    p[1].setValue(p[3])


def p_var_ID(p):
    'var : ID'
    if p[1] in vtable:
        if vtable[p[1]] == 'INT':
            for var in ints:
                if var.getId() == p[1]:
                    p[0] = var
        if vtable[p[1]] == 'FLOAT':
            for var in floats:
                if var.getId() == p[1]:
                    p[0] = var



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
    p[0] = p[1]


def p_simple_expression_1(p):
    'simple_expression : additive_expression checkop additive_expression'


def p_simple_expression_2(p):
    'simple_expression : additive_expression'
    p[0] = p[1]


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
    """
    if isinstance(p[3],Int):
        p[3] = p[3].getValue()
    if isinstance(p[1],Int):
        p[1] = p[1].getValue()   
    if p[2] == '+':
        p[0] = p[1] * p[3]
    elif p[2] == '-': 
        p[0] = p[1] / p[3]


def p_additive_justerm(p):
    'additive_expression : term'
    p[0] = p[1]

def p_addop(p):
    '''addop : PLUS
    | MINUS
    '''
    p[0] = p[1]

def p_factor(p):
    """
    factor : var
           | NUMBER
           | FLOAT
    """
    p[0] = p[1]

def p_factor_1(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_call(p):
    'call : CALL LPAREN ID RPAREN'
    pass


def p_term_mulop(p):
    """
    term : term mulop factor
    """
    if isinstance(p[3],Int):
        p[3] = p[3].getValue()
    if isinstance(p[1],Int):
        p[1] = p[1].getValue()  
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/': 
        p[0] = p[1] / p[3]
    

def p_term_mulop1(p):
    'term : factor'
    p[0] = p[1]
    
def p_mulop(p):
    '''mulop :  TIMES
                | DIVIDE
    '''
    p[0] = p[1]


 # BUild the parser
import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = open('cuadruplos.txt', 'r').read()
        input("OUTPUT:")
        vtable = {}       
        ints = []
        floats = [] 
    except EOFError:
        break
    parser.parse(s) 

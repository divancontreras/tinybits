from tinybit_lex import tokens

precedence = (
    ('left', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('left', 'EXP', 'MOD'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS'),
)


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
    'program : START program_start END'
    pass


def p_program_begin(p):
    'program_start : program_sequence main_declaration'
    pass   


def p_program_sequence(p):
    'program_sequence : program_sequence declaration' 
    pass


def p_declaration_empty(p):
    'program_sequence : empty'


def p_declaration(p):
    """declaration : procces_declaration
    | var_declaration
    """
    pass


def p_var_declaration(p):
    '''var_declaration : var_type ID
    | var_type ID COMMA ID
    | var_type ID EQUAL NUMBER
    | var_type ID EQUAL var
    '''
    pass

def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''

def p_var_type_INT(p):
    'var_type : INT'
    pass


def p_var_type_FLOAT(p):
    'var_type : FLOAT'
    pass


def p_var_declaration_array(p):
    'var_declaration : var_type ID LBRACKET NUMBER RBRACKET'
    pass

def p_main_declaration(p):
    'main_declaration : MAIN ID COLON statements_nont END'
    pass


def p_procces_declaration(p):
    'procces_declaration : PROCCES ID COLON statements_nont END'
    pass


def p_statements_nont(p):
    '''
    statements_nont : statement
                   | statements_nont statement
    '''
    pass


def p_statement(p):
    '''statement : expression
            | condition_nont
            | iteration_nont
            | var_declaration
    '''
    pass

def p_expression(p):
    '''
    expression : primitive
               | STRING
               | ID
    '''
    pass

def p_expression_boolean(p):
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

def p_expression_operation(p):
    '''
    expression : expression PLUS expression %prec PLUS
            | expression MINUS expression %prec MINUS
            | expression MUL expression %prec MUL
            | expression DIV expression %prec DIV
            | expression EXP expression %prec EXP
            | expression MOD expression %prec MOD
    '''
    pass

def p_expression_SETOUT(p):
    '''statement : SETOUT LPAREN QUOTES ID QUOTES RPAREN 
    | SETOUT LPAREN QUOTES ID QUOTES COMMA ENDL RPAREN 
    | SETOUT LPAREN var RPAREN
    | SETOUT LPAREN var COMMA ENDL RPAREN 
    | SETOUT LPAREN var COMMA var COMMA RPAREN 
    | SETOUT LPAREN var COMMA var COMMA ENDL RPAREN 
    '''
    pass


def p_expression_GETIN(p):
    '''expression : GETIN LPAREN var RPAREN
    | GETIN LPAREN var COMMA var RPAREN
    '''
    pass

def p_assign(p):
    '''
    expression : ID EQUALS assignable STMT_END
    '''
    pass

def p_in_expression(p):
    '''
    expression : expression IN expression
               | expression NOT IN expression
    '''
    pass

def p_arrays(p):
    '''
    expression : LBRACKET arguments RBRACKET
    '''
    pass

def p_array_access_assign(p):
    '''
    statement : ID LBRACKET expression RBRACKET EQUALS expression STMT_END
    '''

def p_array_access(p):
    '''
    expression : ID LBRACKET expression RBRACKET
    '''
    pass

def p_compound_operations(p):
    '''
    statement : ID PLUS_EQ expresfsion STMT_END
               | ID MINUS_EQ expression STMT_END
               | ID MUL_EQ expression STMT_END
               | ID DIV_EQ expression STMT_END
               | ID EXP_EQ expression STMT_END
               | ID MOD_EQ expression STMT_END
    '''

def p_expression_overload(p):
    """
    expression : ID DOUBLE_PLUS
               | ID DOUBLE_MINUS
    """
    pass

def p_union_operation(p):
    '''
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
               | NOT expression
    '''

def p_condition_if(p):
    'condition_nont : IF expression THEN statement END'
    pass


def p_condition_if_else(p):
    'condition_nont : IF expression THEN statement ELSE statement END'
    pass


def p_iteration_while(p):
    'iteration_nont : WHILE expression DO statement LOOP'
    pass

def p_procces_call(p):
    '''
    expression : ID LPAREN arguments RPAREN
    statement : ID LPAREN arguments RPAREN STMT_END
    '''
    pass
def p_paren(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    pass





def p_var_ID(p):
    'var : ID'
    pass


def p_var_bracket(p):
    'var : ID LBRACKET expression RBRACKET'
    pass



 # BUild the parser
import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        input("OUTPUT:")
        s = open('codehw.txt', 'r').read()
    except EOFError:
        break
    parser.parse(s) 
import ply.yacc as yacc
from examplelex import tokens


precedence = (
    ('left', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('left', 'EXP', 'MOD'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS'),
)


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


def p_identifier(p):
    '''
    identifier : IDENTIFIER
    '''
    pass

def p_primitive(p):
    '''
    primitive : NUM_INT
              | NUM_FLOAT
              | STRING
              | boolean
    '''
    pass


def p_binary_op(p):
    '''
    expression : expression PLUS expression %prec PLUS
            | expression MINUS expression %prec MINUS
            | expression MUL expression %prec MUL
            | expression DIV expression %prec DIV
            | expression EXP expression %prec EXP
            | expression MOD expression %prec MOD
            | expression BIT_AND expression
            | expression BIT_OR expression
            | expression BIT_XOR expression
            | expression LSHIFT expression
            | expression RSHIFT expression
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
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
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

def p_compound_operations(p):
    '''
    statement : identifier PLUS_EQ expression 
               | identifier MINUS_EQ expression 
               | identifier MUL_EQ expression 
               | identifier DIV_EQ expression 
               | identifier EXP_EQ expression 
               | identifier MOD_EQ expression 
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
               | STRING
               | identifier
    '''
    pass

def p_for_loop(p):
    '''
    statement : FOR identifier IN expression ARROW_LTR expression DO statement_list END
              | FOR identifier IN expression ARROW_RTL expression DO statement_list END
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
              | PROCCES identifier COLON statement_list END
    '''
    pass


def p_procces_call(p):
    '''
    expression : identifier ARROW_LTR START
    statement : identifier ARROW_LTR START
    '''
    pass


def p_error(p):
    if p is not None:
        raise ParserSyntaxError("Syntax error at line %d, illegal token '%s' found" % (p.lineno, p.value))

    raise ParserSyntaxError("Unexpected end of input")


def get_parser():
    return yacc.yacc(errorlog=yacc.NullLogger()) if disable_warnings else yacc.yacc()
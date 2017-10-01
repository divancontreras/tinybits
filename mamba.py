import ply.yacc as yacc
from mambalex import tokens

VERBOSE = 1

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


def p_statement(p):
    '''
    statement : identifier
              | expression
              | if_statement
    '''


def p_identifier(p):
    '''
    identifier : IDENTIFIER
    '''


def p_exit_stmt(p):
    '''
    statement : EXIT STMT_END
    '''


def p_primitive(p):
    '''
    primitive : NUM_INT
              | NUM_FLOAT
              | STRING
              | boolean
    '''


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


def p_unary_operation(p):
    '''
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
               | BIT_NEG expression
               | NOT expression
    '''


def p_paren(p):
    '''
    expression : LPAREN expression RPAREN
    '''


def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''


def p_assignable(p):
    '''
    assignable : primitive
               | expression
    '''


def p_comma_separated_expr(p):
    '''
    arguments : arguments COMMA expression
              | expression
              |
    '''


def p_ternary_op(p):
    '''
    expression : expression QUESTION_MARK expression COLON expression
    '''

def p_arrays(p):
    '''
    expression : LSQBRACK arguments RSQBRACK
    '''


def p_array_access(p):
    '''
    expression : identifier LSQBRACK expression RSQBRACK
    '''


def p_slice(p):
    '''
    expression : identifier LSQBRACK expression COLON expression RSQBRACK
               | identifier LSQBRACK COLON expression RSQBRACK
               | identifier LSQBRACK expression COLON RSQBRACK
               | identifier LSQBRACK COLON RSQBRACK
    '''

def p_array_access_assign(p):
    '''
    statement : identifier LSQBRACK expression RSQBRACK EQUALS expression STMT_END
    '''


def p_assign(p):
    '''
    expression : identifier EQUALS assignable STMT_END
    '''


def p_ifstatement(p):
    '''
    if_statement : IF expression LBRACK statement_list RBRACK
    '''


def p_ifstatement_else(p):
    '''
    if_statement : IF expression LBRACK statement_list RBRACK ELSE LBRACK statement_list RBRACK
    '''


def p_ifstatement_else_if(p):
    '''
    if_statement : IF expression LBRACK statement_list RBRACK ELSE if_statement
    '''


def p_in_expression(p):
    '''
    expression : expression IN expression
               | expression NOT IN expression
    '''


def p_print_statement(p):
    '''
    statement : PRINT arguments STMT_END
    '''


def p_compound_operations(p):
    '''
    statement : identifier PLUS_EQ expression STMT_END
               | identifier MINUS_EQ expression STMT_END
               | identifier MUL_EQ expression STMT_END
               | identifier DIV_EQ expression STMT_END
               | identifier EXP_EQ expression STMT_END
               | identifier MOD_EQ expression STMT_END
    '''


def p_increment_decrement_identifiers(p):
    '''
    expression : identifier DOUBLE_PLUS
               | identifier DOUBLE_MINUS
    '''

def p_expression(p):
    '''
    expression : primitive
               | STRING
               | identifier
    '''


def p_for_loop(p):
    '''
    statement : FOR identifier IN expression ARROW_LTR expression LBRACK statement_list RBRACK
              | FOR identifier IN expression ARROW_RTL expression LBRACK statement_list RBRACK
    '''


def p_for_in_loop(p):
    '''
    statement : FOR identifier IN expression LBRACK statement_list RBRACK
    '''


def p_while_loop(p):
    '''
    statement : WHILE expression LBRACK statement_list RBRACK
    '''


def p_for_loop_infinite(p):
    '''
    statement : FOR LBRACK statement_list RBRACK
    '''


def p_function_declaration(p):
    '''
    statement : FUNCTION identifier LPAREN arguments RPAREN LBRACK statement_list RBRACK
              | FUNCTION identifier LBRACK statement_list RBRACK
    '''


def p_return(p):
    '''
    statement : RETURN expression STMT_END
    '''


def p_function_call(p):
    '''
    expression : identifier LPAREN arguments RPAREN
    statement : identifier LPAREN arguments RPAREN STMT_END
    '''



def p_error(p):
    if VERBOSE:
        if p is not None:
            print ("Error en Sintaxis linea:" + str(p.lexer.lineno)+"  Error de Contexto " + str(p.value))
        else:
            print ("Error en Lexico linea: " + str(c_lexer.lexer.lineno))
    else:
        raise Exception('Syntax', 'error')


parser = yacc.yacc(debug=True)

with open ("codehw.txt", "r") as myfile:
     data = str(myfile.readlines())

yacc.parse(data)


import ply.yacc as yacc
import ast
from ast import context
from tinybit_lex_ast import *
from tinybit_errors import *
import environment
disable_warnings = False
import pprint
VERBOSE = 1

precedence = (
    ('left', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('left', 'EXP', 'MOD'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS'),
)

def p_program(p):
    'program : BEGIN statement_list END'
    res = p[2]
    environment.declare_env(context)
    for node in res:
        node.eval()
    if False:
        print("\n\n" + '=' * 80, ' == Syntax tree ==')
        pp = pprint.PrettyPrinter()
        pp.pprint(res.children)
        #pp.pprint(context.table())

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    else:
        p[1].children.append(p[2])
        p[0] = p[1]


def p_statement(p):
    '''
    statement : identifier
              | expression
              | if_statement
    '''
    p[0] = p[1]


def p_identifier(p):
    '''
    identifier : IDENTIFIER
    '''
    p[0] = ast.Identifier(p[1])


def p_exit_(p):
    '''
    statement : EXIT 
    '''
    p[0] = ast.ExitStatement()


def p_primitive(p):
    '''
    primitive : NUM_INT
              | NUM_FLOAT
              | STRING
              | boolean
    '''
    if isinstance(p[1], ast.BaseExpression):
        p[0] = p[1]
    else:
        p[0] = ast.Primitive(p[1])


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
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])

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
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])

def p_unary_operation(p):
    '''
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
               | BIT_NEG expression
               | NOT expression
    '''
    p[0] = ast.UnaryOperation(p[1], p[2])


def p_paren(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2] if isinstance(p[2], ast.BaseExpression) else ast.Primitive(p[2])


def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''
    p[0] = ast.Primitive(p[1])


def p_assignable(p):
    '''
    assignable : primitive
               | expression
    '''
    p[0] = p[1]


def p_comma_separated_expr(p):
    '''
    arguments : arguments COMMA expression
              | expression
              |
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    elif len(p) == 1:
        p[0] = ast.InstructionList()
    else:
        p[1].children.append(p[3])
        p[0] = p[1]

def p_arrays(p):
    '''
    expression : LSQBRACK arguments RSQBRACK
    '''
    p[0] = ast.Array(p[2])


def p_array_access(p):
    '''
    expression : identifier LSQBRACK expression RSQBRACK
    '''
    p[0] = ast.ArrayAccess(p[1], p[3])


def p_slice(p):
    '''
    expression : identifier LSQBRACK expression COLON expression RSQBRACK
               | identifier LSQBRACK COLON expression RSQBRACK
               | identifier LSQBRACK expression COLON RSQBRACK
               | identifier LSQBRACK COLON RSQBRACK
    '''
    if len(p) == 7:
        p[0] = ast.ArraySlice(p[1], p[3], p[5])
    elif len(p) == 5:
        p[0] = ast.ArraySlice(p[1])
    elif p[3] == ':':
        # accessing [:expr]
        p[0] = ast.ArraySlice(p[1], end=p[4])
    else:
        # accessing [expr:]
        p[0] = ast.ArraySlice(p[1], start=p[3])


def p_array_access_assign(p):
    '''
    statement : identifier LSQBRACK expression RSQBRACK EQUALS expression 
    '''
    p[0] = ast.ArrayAssign(p[1], p[3], p[6])


def p_assign(p):
    '''
    expression : identifier EQUALS assignable 
    '''
    p[0] = ast.Assignment(p[1], p[3])


def p_ifstatement(p):
    '''
    if_statement : IF expression THEN LBRACK statement_list RBRACK
    '''
    p[0] = ast.If(p[2], p[5])


def p_ifstatement_else(p):
    '''
    if_statement : IF expression THEN LBRACK statement_list RBRACK ELSE LBRACK statement_list RBRACK
    '''
    p[0] = ast.If(p[2], p[5], p[9])


def p_ifstatement_else_if(p):
    '''
    if_statement : IF expression THEN LBRACK statement_list RBRACK ELSE if_statement
    '''
    p[0] = ast.If(p[2], p[5], p[8])


def p_in_expression(p):
    '''
    expression : expression IN expression
               | expression NOT IN expression
    '''
    if len(p) == 4:
        p[0] = ast.InExpression(p[1], p[3])
    else:
        p[0] = ast.InExpression(p[1], p[4], True)


def p_print_statement(p):
    '''
    statement : SETOUT LPAREN arguments RPAREN
    '''
    p[0] = ast.PrintStatement(p[3])


def p_input_statement(p):
    '''
    statement : GETIN LPAREN identifier RPAREN
    '''
    p[0] = ast.InputStatement(p[3])


def p_compound_operations(p):
    '''
    statement : identifier PLUS_EQ expression 
               | identifier MINUS_EQ expression 
               | identifier MUL_EQ expression 
               | identifier DIV_EQ expression 
               | identifier EXP_EQ expression 
               | identifier MOD_EQ expression 
    '''
    p[0] = ast.CompoundOperation(p[1], p[3], p[2])


def p_increment_decrement_identifiers(p):
    '''
    expression : identifier PLUS_EQUAL NUM_INT
               | identifier MINUS_EQUAL NUM_INT
    '''
    if p[2] == '+=':
        p[0] = ast.Assignment(p[1], ast.BinaryOperation(p[1], ast.Primitive(p[3]), '+'))
    else:
        p[0] = ast.Assignment(p[1], ast.BinaryOperation(p[1], ast.Primitive(p[3]), '-'))


def p_expression(p):
    '''
    expression : primitive
               | STRING
               | identifier
    '''
    p[0] = p[1]


def p_for_loop(p):
    '''
    statement : FOR identifier IN expression ARROW_LTR expression DO LBRACK statement_list RBRACK
              | FOR identifier IN expression ARROW_RTL expression DO LBRACK statement_list RBRACK
    '''
    p[0] = ast.For(p[2], p[4], p[6], p[5] == '->', p[9])

def p_for_in_loop(p):
    '''
    statement : FOR identifier IN expression LBRACK statement_list RBRACK
    '''
    p[0] = ast.ForIn(p[2], p[4], p[6])


def p_while_loop(p):
    '''
    statement : WHILE expression DO LBRACK statement_list RBRACK
    '''
    p[0] = ast.While(p[2], p[5])


def p_function_declaration(p):
    '''
    statement : PROCESS identifier DO LBRACK statement_list RBRACK
    '''
    p[2].is_function = True

    if len(p) == 9:
        p[0] = ast.Assignment(p[2], ast.Function(p[4], p[7]))
    else:
        p[0] = ast.Assignment(p[2], ast.Function(ast.InstructionList(), p[4]))



def p_function_call(p):
    '''
    expression : identifier LPAREN arguments RPAREN
    statement : identifier LPAREN arguments RPAREN 
    '''
    p[1].is_function = True
    p[0] = ast.FunctionCall(p[1], p[3])

def p_error(p):
    if VERBOSE:
        if p is not None:
            print ("Error en Sintaxis linea:" + str(p.lexer.lineno)+"  Error de Contexto " + str(p.value))
        else:
            print ("Error en Lexico linea: " + str(c_lexer.lexer.lineno))
    else:
        raise Exception('Syntax', 'error')

parser = yacc.yacc()

s = open('codetry.tb', 'r').read()
    
parser.parse(s) 

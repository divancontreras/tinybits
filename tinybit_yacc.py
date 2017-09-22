from tinybit_lex import tokens


def p_error(t):
    print("INPUT RECHAZADO")


def p_program(p):
    'program : program_begin'
    pass


def p_program_begin(p):

    'program_begin : program_sequence'
  
    pass   

def p_program_sequence(p):

	'program_sequence : declaration program_sequence' 

    pass   

def p_declaration(p):

    	"""declaration : var_declaration
		| process_declaration
		"""
    pass

def p_var_declaration(p):
    '''var_declaration : type_specifier ID
    | var_type ID COMMA ID
    | var_type ID EQUAL NUMBER
    | var_type ID EQUAL var
    '''
    pass

def p_var_declaration_array(p):
    'var_declaration : var_type ID LBRACKET NUMBER RBRACKET'
    pass


 # BUild the parser
import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('>> ')  
    except EOFError:
        break
    parser.parse(s)

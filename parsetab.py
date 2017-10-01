
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'START END SETOUT GETIN DO LOOP EQUALS PROCCES IDENTIFIER NUM_INT NUM_FLOAT LPAREN RPAREN THEN COMMA LSQBRACK RSQBRACK MAIN COLON PLUS EXP MINUS MUL DIV MOD BIT_AND BIT_OR BIT_NEG DOUBLE_PLUS DOUBLE_MINUS TRUE FALSE EQ NEQ GT GTE LT LTE ARROW_LTR ARROW_RTL IF ELSE IN FOR WHILE AND OR NOT\n    statement_list : statement\n                   | statement_list statement\n    \n    statement : identifier\n              | expression\n              | if_statement\n    \n    identifier : IDENTIFIER\n    \n    primitive : NUM_INT\n              | NUM_FLOAT\n              | boolean\n    \n    expression : expression PLUS expression PLUS\n            | expression MINUS expression MINUS\n            | expression MUL expression MUL\n            | expression DIV expression DIV\n            | expression EXP expression EXP\n            | expression MOD expression MOD\n            | expression BIT_AND expression\n            | expression BIT_OR expression\n\n    \n    boolean : expression EQ expression\n            | expression NEQ expression\n            | expression GT expression\n            | expression GTE expression\n            | expression LT expression\n            | expression LTE expression\n            | expression AND expression\n            | expression OR expression\n    \n    expression : MINUS expression MINUS\n               | PLUS expression PLUS\n               | BIT_NEG expression\n               | NOT expression\n    \n    expression : LPAREN expression RPAREN\n    \n    boolean : TRUE\n            | FALSE\n    \n    assignable : primitive\n               | expression\n    \n    arguments : arguments COMMA expression\n              | expression\n              | \n    \n    expression : LSQBRACK arguments RSQBRACK\n    \n    expression : identifier LSQBRACK expression RSQBRACK\n    \n    expression : identifier LSQBRACK expression COLON expression RSQBRACK\n               | identifier LSQBRACK COLON expression RSQBRACK\n               | identifier LSQBRACK expression COLON RSQBRACK\n               | identifier LSQBRACK COLON RSQBRACK\n    \n    statement : identifier LSQBRACK expression RSQBRACK EQUALS expression \n    \n    expression : identifier EQUALS assignable\n    \n    if_statement : IF expression THEN statement_list END\n    \n    if_statement : IF expression THEN statement_list ELSE statement_list END\n    \n    if_statement : IF expression THEN statement_list ELSE if_statement\n    \n    expression : expression IN expression\n               | expression NOT IN expression\n    \n    statement : SETOUT arguments\n    \n    statement : GETIN arguments\n    \n    expression : identifier DOUBLE_PLUS\n               | identifier DOUBLE_MINUS\n    \n    expression : primitive\n               | identifier\n    \n    statement : FOR identifier IN expression ARROW_LTR expression DO statement_list LOOP\n              | FOR identifier IN expression ARROW_RTL expression DO statement_list LOOP\n    \n    statement : FOR identifier IN expression DO statement_list LOOP\n    \n    statement : WHILE expression DO statement_list LOOP\n    \n    statement : PROCCES identifier COLON statement_list END\n    \n    expression : PROCCES identifier ARROW_LTR START\n    statement : PROCCES identifier ARROW_LTR START\n    '
    
_lr_action_items = {'SETOUT':([0,1,2,3,4,5,7,8,12,18,20,21,22,23,24,25,28,29,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,91,92,94,95,96,97,98,101,102,103,104,105,106,107,108,109,113,114,115,116,119,120,121,122,124,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[7,7,-1,-3,-4,-5,-37,-37,-6,-55,-7,-8,-9,-31,-32,-2,-53,-54,-36,-56,-51,-52,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,7,7,-27,-26,-30,7,-39,-43,-10,-11,-12,-13,-14,-15,-50,-35,7,7,-62,7,-42,-41,-39,-62,7,-60,-61,-46,7,-44,-40,7,7,-5,7,-59,7,-47,7,7,-57,-58,]),'GETIN':([0,1,2,3,4,5,7,8,12,18,20,21,22,23,24,25,28,29,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,91,92,94,95,96,97,98,101,102,103,104,105,106,107,108,109,113,114,115,116,119,120,121,122,124,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[8,8,-1,-3,-4,-5,-37,-37,-6,-55,-7,-8,-9,-31,-32,-2,-53,-54,-36,-56,-51,-52,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,8,8,-27,-26,-30,8,-39,-43,-10,-11,-12,-13,-14,-15,-50,-35,8,8,-62,8,-42,-41,-39,-62,8,-60,-61,-46,8,-44,-40,8,8,-5,8,-59,8,-47,8,8,-57,-58,]),'FOR':([0,1,2,3,4,5,7,8,12,18,20,21,22,23,24,25,28,29,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,91,92,94,95,96,97,98,101,102,103,104,105,106,107,108,109,113,114,115,116,119,120,121,122,124,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[9,9,-1,-3,-4,-5,-37,-37,-6,-55,-7,-8,-9,-31,-32,-2,-53,-54,-36,-56,-51,-52,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,9,9,-27,-26,-30,9,-39,-43,-10,-11,-12,-13,-14,-15,-50,-35,9,9,-62,9,-42,-41,-39,-62,9,-60,-61,-46,9,-44,-40,9,9,-5,9,-59,9,-47,9,9,-57,-58,]),'WHILE':([0,1,2,3,4,5,7,8,12,18,20,21,22,23,24,25,28,29,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,91,92,94,95,96,97,98,101,102,103,104,105,106,107,108,109,113,114,115,116,119,120,121,122,124,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[10,10,-1,-3,-4,-5,-37,-37,-6,-55,-7,-8,-9,-31,-32,-2,-53,-54,-36,-56,-51,-52,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,10,10,-27,-26,-30,10,-39,-43,-10,-11,-12,-13,-14,-15,-50,-35,10,10,-62,10,-42,-41,-39,-62,10,-60,-61,-46,10,-44,-40,10,10,-5,10,-59,10,-47,10,10,-57,-58,]),'PROCCES':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,59,60,64,65,66,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[11,11,-1,-3,-4,-5,51,51,51,51,-6,51,51,51,51,51,-55,51,-7,-8,-9,-31,-32,-2,51,51,-53,-54,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-36,-56,-51,-52,-28,-29,51,-45,-33,-34,-16,-17,-49,51,-18,-19,-20,-21,-22,-23,-24,-25,-38,51,51,51,11,11,51,51,-30,11,-39,51,-43,51,51,51,51,51,51,-50,-35,11,11,-62,11,51,-42,-41,-39,-62,51,11,51,-60,-61,-46,11,-44,-40,11,11,-5,11,-59,11,-47,11,11,-57,-58,]),'IDENTIFIER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,51,52,53,59,60,64,65,66,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[12,12,-1,-3,-4,-5,12,12,12,12,12,12,-6,12,12,12,12,12,-55,12,-7,-8,-9,-31,-32,-2,12,12,-53,-54,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-36,-56,12,-51,-52,-28,-29,12,-45,-33,-34,-16,-17,-49,12,-18,-19,-20,-21,-22,-23,-24,-25,-38,12,12,12,12,12,12,12,-30,12,-39,12,-43,12,12,12,12,12,12,-50,-35,12,12,-62,12,12,-42,-41,-39,-62,12,12,12,-60,-61,-46,12,-44,-40,12,12,-5,12,-59,12,-47,12,12,-57,-58,]),'MINUS':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,],[14,14,-1,-3,31,-5,14,14,14,14,-6,14,14,14,14,14,-55,14,-7,-8,-9,-31,-32,-2,14,14,-53,-54,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,31,-56,-51,-52,31,31,95,31,31,31,31,31,14,-45,-33,31,31,103,31,31,31,31,31,31,31,14,31,31,31,31,31,31,31,31,-38,14,14,14,14,14,14,14,-30,14,-39,14,31,-43,14,14,14,14,14,14,31,31,31,31,14,14,-62,14,14,31,-42,-41,-39,-62,14,14,14,-60,-61,-46,14,31,-40,31,14,31,14,-5,14,-59,14,-47,14,14,-57,-58,]),'PLUS':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,],[13,13,-1,-3,30,-5,13,13,13,13,-6,13,13,13,13,13,-55,13,-7,-8,-9,-31,-32,-2,13,13,-53,-54,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,30,-56,-51,-52,30,94,30,30,30,30,30,30,13,-45,-33,30,102,30,30,30,30,30,30,30,30,13,30,30,30,30,30,30,30,30,-38,13,13,13,13,13,13,13,-30,13,-39,13,30,-43,13,13,13,13,13,13,30,30,30,30,13,13,-62,13,13,30,-42,-41,-39,-62,13,13,13,-60,-61,-46,13,30,-40,30,13,30,13,-5,13,-59,13,-47,13,13,-57,-58,]),'BIT_NEG':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,59,60,64,65,66,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[15,15,-1,-3,-4,-5,15,15,15,15,-6,15,15,15,15,15,-55,15,-7,-8,-9,-31,-32,-2,15,15,-53,-54,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-36,-56,-51,-52,-28,-29,15,-45,-33,-34,-16,-17,-49,15,-18,-19,-20,-21,-22,-23,-24,-25,-38,15,15,15,15,15,15,15,-30,15,-39,15,-43,15,15,15,15,15,15,-50,-35,15,15,-62,15,15,-42,-41,-39,-62,15,15,15,-60,-61,-46,15,-44,-40,15,15,-5,15,-59,15,-47,15,15,-57,-58,]),'NOT':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,],[16,16,-1,-3,39,-5,16,16,16,16,-6,16,16,16,16,16,-55,16,-7,-8,-9,-31,-32,-2,16,16,-53,-54,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,39,-56,-51,-52,39,39,39,39,39,39,39,39,16,-45,-33,39,39,39,39,39,39,39,39,39,39,16,39,39,39,39,39,39,39,39,-38,16,16,16,16,16,16,16,-30,16,-39,16,39,-43,16,16,16,16,16,16,39,39,39,39,16,16,-62,16,16,39,-42,-41,-39,-62,16,16,16,-60,-61,-46,16,39,-40,39,16,39,16,-5,16,-59,16,-47,16,16,-57,-58,]),'LPAREN':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,59,60,64,65,66,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[17,17,-1,-3,-4,-5,17,17,17,17,-6,17,17,17,17,17,-55,17,-7,-8,-9,-31,-32,-2,17,17,-53,-54,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-36,-56,-51,-52,-28,-29,17,-45,-33,-34,-16,-17,-49,17,-18,-19,-20,-21,-22,-23,-24,-25,-38,17,17,17,17,17,17,17,-30,17,-39,17,-43,17,17,17,17,17,17,-50,-35,17,17,-62,17,17,-42,-41,-39,-62,17,17,17,-60,-61,-46,17,-44,-40,17,17,-5,17,-59,17,-47,17,17,-57,-58,]),'LSQBRACK':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,59,60,64,65,66,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[6,6,-1,26,-4,-5,6,6,6,6,-6,6,6,6,6,6,-55,6,-7,-8,-9,-31,-32,-2,6,6,-53,-54,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-36,88,-51,-52,-28,-29,6,-45,-33,-34,-16,-17,-49,6,-18,-19,-20,-21,-22,-23,-24,-25,-38,6,6,6,6,6,6,6,-30,6,-39,6,-43,6,6,6,6,6,6,-50,-35,6,6,-62,6,6,-42,-41,-39,-62,6,6,6,-60,-61,-46,6,-44,-40,6,6,-5,6,-59,6,-47,6,6,-57,-58,]),'IF':([0,1,2,3,4,5,7,8,12,18,20,21,22,23,24,25,28,29,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,91,92,94,95,96,97,98,101,102,103,104,105,106,107,108,109,113,114,115,116,119,120,121,122,124,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[19,19,-1,-3,-4,-5,-37,-37,-6,-55,-7,-8,-9,-31,-32,-2,-53,-54,-36,-56,-51,-52,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,19,19,-27,-26,-30,19,-39,-43,-10,-11,-12,-13,-14,-15,-50,-35,19,19,-62,19,-42,-41,-39,-62,19,-60,-61,-46,19,-44,-40,19,19,-5,19,-59,19,-47,19,19,-57,-58,]),'NUM_INT':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,59,60,64,65,66,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[20,20,-1,-3,-4,-5,20,20,20,20,-6,20,20,20,20,20,-55,20,-7,-8,-9,-31,-32,-2,20,20,-53,-54,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-36,-56,-51,-52,-28,-29,20,-45,-33,-34,-16,-17,-49,20,-18,-19,-20,-21,-22,-23,-24,-25,-38,20,20,20,20,20,20,20,-30,20,-39,20,-43,20,20,20,20,20,20,-50,-35,20,20,-62,20,20,-42,-41,-39,-62,20,20,20,-60,-61,-46,20,-44,-40,20,20,-5,20,-59,20,-47,20,20,-57,-58,]),'NUM_FLOAT':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,59,60,64,65,66,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[21,21,-1,-3,-4,-5,21,21,21,21,-6,21,21,21,21,21,-55,21,-7,-8,-9,-31,-32,-2,21,21,-53,-54,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-36,-56,-51,-52,-28,-29,21,-45,-33,-34,-16,-17,-49,21,-18,-19,-20,-21,-22,-23,-24,-25,-38,21,21,21,21,21,21,21,-30,21,-39,21,-43,21,21,21,21,21,21,-50,-35,21,21,-62,21,21,-42,-41,-39,-62,21,21,21,-60,-61,-46,21,-44,-40,21,21,-5,21,-59,21,-47,21,21,-57,-58,]),'TRUE':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,59,60,64,65,66,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[23,23,-1,-3,-4,-5,23,23,23,23,-6,23,23,23,23,23,-55,23,-7,-8,-9,-31,-32,-2,23,23,-53,-54,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-36,-56,-51,-52,-28,-29,23,-45,-33,-34,-16,-17,-49,23,-18,-19,-20,-21,-22,-23,-24,-25,-38,23,23,23,23,23,23,23,-30,23,-39,23,-43,23,23,23,23,23,23,-50,-35,23,23,-62,23,23,-42,-41,-39,-62,23,23,23,-60,-61,-46,23,-44,-40,23,23,-5,23,-59,23,-47,23,23,-57,-58,]),'FALSE':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,49,50,52,53,59,60,64,65,66,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,133,135,136,137,138,139,140,141,142,143,144,],[24,24,-1,-3,-4,-5,24,24,24,24,-6,24,24,24,24,24,-55,24,-7,-8,-9,-31,-32,-2,24,24,-53,-54,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-36,-56,-51,-52,-28,-29,24,-45,-33,-34,-16,-17,-49,24,-18,-19,-20,-21,-22,-23,-24,-25,-38,24,24,24,24,24,24,24,-30,24,-39,24,-43,24,24,24,24,24,24,-50,-35,24,24,-62,24,24,-42,-41,-39,-62,24,24,24,-60,-61,-46,24,-44,-40,24,24,-5,24,-59,24,-47,24,24,-57,-58,]),'$end':([1,2,3,4,5,7,8,12,18,20,21,22,23,24,25,28,29,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,101,102,103,104,105,106,107,108,109,115,119,120,121,122,126,127,128,130,131,136,138,140,143,144,],[0,-1,-3,-4,-5,-37,-37,-6,-55,-7,-8,-9,-31,-32,-2,-53,-54,-36,-56,-51,-52,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,-39,-43,-10,-11,-12,-13,-14,-15,-50,-35,-62,-42,-41,-39,-62,-60,-61,-46,-44,-40,-48,-59,-47,-57,-58,]),'LOOP':([2,3,4,5,7,8,12,18,20,21,22,23,24,25,28,29,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,101,102,103,104,105,106,107,108,109,113,115,119,120,121,122,126,127,128,130,131,133,136,138,140,141,142,143,144,],[-1,-3,-4,-5,-37,-37,-6,-55,-7,-8,-9,-31,-32,-2,-53,-54,-36,-56,-51,-52,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,-39,-43,-10,-11,-12,-13,-14,-15,-50,-35,126,-62,-42,-41,-39,-62,-60,-61,-46,-44,-40,138,-48,-59,-47,143,144,-57,-58,]),'END':([2,3,4,5,7,8,12,18,20,21,22,23,24,25,28,29,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,101,102,103,104,105,106,107,108,109,114,115,116,119,120,121,122,126,127,128,130,131,135,136,138,140,143,144,],[-1,-3,-4,-5,-37,-37,-6,-55,-7,-8,-9,-31,-32,-2,-53,-54,-36,-56,-51,-52,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,-39,-43,-10,-11,-12,-13,-14,-15,-50,-35,127,-62,128,-42,-41,-39,-62,-60,-61,-46,-44,-40,140,-5,-59,-47,-57,-58,]),'ELSE':([2,3,4,5,7,8,12,18,20,21,22,23,24,25,28,29,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,101,102,103,104,105,106,107,108,109,115,116,119,120,121,122,126,127,128,130,131,136,138,140,143,144,],[-1,-3,-4,-5,-37,-37,-6,-55,-7,-8,-9,-31,-32,-2,-53,-54,-36,-56,-51,-52,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,-39,-43,-10,-11,-12,-13,-14,-15,-50,-35,-62,129,-42,-41,-39,-62,-60,-61,-46,-44,-40,-48,-59,-47,-57,-58,]),'EQUALS':([3,12,50,98,],[27,-6,27,117,]),'DOUBLE_PLUS':([3,12,50,],[28,-6,28,]),'DOUBLE_MINUS':([3,12,50,],[29,-6,29,]),'MUL':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,32,-6,-55,-7,-8,-9,-31,-32,-53,-54,32,-56,32,32,32,32,32,32,32,32,-45,-33,32,32,32,104,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-38,-27,-26,-30,-39,32,-43,-10,-11,-12,-13,-14,-15,32,32,32,32,-62,32,-42,-41,-39,-62,32,-40,32,32,]),'DIV':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,33,-6,-55,-7,-8,-9,-31,-32,-53,-54,33,-56,33,33,33,33,33,33,33,33,-45,-33,33,33,33,33,105,33,33,33,33,33,33,33,33,33,33,33,33,33,-38,-27,-26,-30,-39,33,-43,-10,-11,-12,-13,-14,-15,33,33,33,33,-62,33,-42,-41,-39,-62,33,-40,33,33,]),'EXP':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,34,-6,-55,-7,-8,-9,-31,-32,-53,-54,34,-56,34,34,34,34,34,34,34,34,-45,-33,34,34,34,34,34,106,34,34,34,34,34,34,34,34,34,34,34,34,-38,-27,-26,-30,-39,34,-43,-10,-11,-12,-13,-14,-15,34,34,34,34,-62,34,-42,-41,-39,-62,34,-40,34,34,]),'MOD':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,35,-6,-55,-7,-8,-9,-31,-32,-53,-54,35,-56,35,35,35,35,35,35,35,35,-45,-33,35,35,35,35,35,35,107,35,35,35,35,35,35,35,35,35,35,35,-38,-27,-26,-30,-39,35,-43,-10,-11,-12,-13,-14,-15,35,35,35,35,-62,35,-42,-41,-39,-62,35,-40,35,35,]),'BIT_AND':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,36,-6,-55,-7,-8,-9,-31,-32,-53,-54,36,-56,36,36,36,36,36,36,36,36,-45,-33,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-38,-27,-26,-30,-39,36,-43,-10,-11,-12,-13,-14,-15,36,36,36,36,-62,36,-42,-41,-39,-62,36,-40,36,36,]),'BIT_OR':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,37,-6,-55,-7,-8,-9,-31,-32,-53,-54,37,-56,37,37,37,37,37,37,37,37,-45,-33,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-38,-27,-26,-30,-39,37,-43,-10,-11,-12,-13,-14,-15,37,37,37,37,-62,37,-42,-41,-39,-62,37,-40,37,37,]),'IN':([3,4,12,18,20,21,22,23,24,28,29,39,49,50,54,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,38,-6,-55,-7,-8,-9,-31,-32,-53,-54,77,38,-56,90,38,38,38,38,38,38,38,38,-45,-33,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-38,-27,-26,-30,-39,38,-43,-10,-11,-12,-13,-14,-15,38,38,38,38,-62,38,-42,-41,-39,-62,38,-40,38,38,]),'EQ':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,40,-6,-55,-7,-8,-9,-31,-32,-53,-54,40,-56,40,40,40,40,40,40,40,40,-45,-33,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-38,-27,-26,-30,-39,40,-43,-10,-11,-12,-13,-14,-15,40,40,40,40,-62,40,-42,-41,-39,-62,40,-40,40,40,]),'NEQ':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,41,-6,-55,-7,-8,-9,-31,-32,-53,-54,41,-56,41,41,41,41,41,41,41,41,-45,-33,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-38,-27,-26,-30,-39,41,-43,-10,-11,-12,-13,-14,-15,41,41,41,41,-62,41,-42,-41,-39,-62,41,-40,41,41,]),'GT':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,42,-6,-55,-7,-8,-9,-31,-32,-53,-54,42,-56,42,42,42,42,42,42,42,42,-45,-33,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-38,-27,-26,-30,-39,42,-43,-10,-11,-12,-13,-14,-15,42,42,42,42,-62,42,-42,-41,-39,-62,42,-40,42,42,]),'GTE':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,43,-6,-55,-7,-8,-9,-31,-32,-53,-54,43,-56,43,43,43,43,43,43,43,43,-45,-33,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-38,-27,-26,-30,-39,43,-43,-10,-11,-12,-13,-14,-15,43,43,43,43,-62,43,-42,-41,-39,-62,43,-40,43,43,]),'LT':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,44,-6,-55,-7,-8,-9,-31,-32,-53,-54,44,-56,44,44,44,44,44,44,44,44,-45,-33,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-38,-27,-26,-30,-39,44,-43,-10,-11,-12,-13,-14,-15,44,44,44,44,-62,44,-42,-41,-39,-62,44,-40,44,44,]),'LTE':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,45,-6,-55,-7,-8,-9,-31,-32,-53,-54,45,-56,45,45,45,45,45,45,45,45,-45,-33,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-38,-27,-26,-30,-39,45,-43,-10,-11,-12,-13,-14,-15,45,45,45,45,-62,45,-42,-41,-39,-62,45,-40,45,45,]),'AND':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,46,-6,-55,-7,-8,-9,-31,-32,-53,-54,46,-56,46,46,46,46,46,46,46,46,-45,-33,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-38,-27,-26,-30,-39,46,-43,-10,-11,-12,-13,-14,-15,46,46,46,46,-62,46,-42,-41,-39,-62,46,-40,46,46,]),'OR':([3,4,12,18,20,21,22,23,24,28,29,49,50,55,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,98,100,101,102,103,104,105,106,107,108,109,110,112,115,118,119,120,121,122,130,131,132,134,],[-56,47,-6,-55,-7,-8,-9,-31,-32,-53,-54,47,-56,47,47,47,47,47,47,47,47,-45,-33,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-38,-27,-26,-30,-39,47,-43,-10,-11,-12,-13,-14,-15,47,47,47,47,-62,47,-42,-41,-39,-62,47,-40,47,47,]),'RSQBRACK':([6,12,18,20,21,22,23,24,28,29,48,49,50,59,60,63,64,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,99,100,101,102,103,104,105,106,107,108,109,110,118,119,120,121,122,131,],[-37,-6,-55,-7,-8,-9,-31,-32,-53,-54,86,-36,-56,-28,-29,98,101,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,119,120,-43,-10,-11,-12,-13,-14,-15,-50,-35,121,131,-42,-41,-39,-62,-40,]),'COMMA':([6,7,8,12,18,20,21,22,23,24,28,29,48,49,50,52,53,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,101,102,103,104,105,106,107,108,109,119,120,121,122,131,],[-37,-37,-37,-6,-55,-7,-8,-9,-31,-32,-53,-54,87,-36,-56,87,87,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,-43,-10,-11,-12,-13,-14,-15,-50,-35,-42,-41,-39,-62,-40,]),'DO':([12,18,20,21,22,23,24,28,29,50,55,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,101,102,103,104,105,106,107,108,112,119,120,121,122,131,132,134,],[-6,-55,-7,-8,-9,-31,-32,-53,-54,-56,91,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,-43,-10,-11,-12,-13,-14,-15,-50,124,-42,-41,-39,-62,-40,137,139,]),'COLON':([12,18,20,21,22,23,24,26,28,29,50,56,59,60,63,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,88,94,95,96,101,102,103,104,105,106,107,108,110,119,120,121,122,131,],[-6,-55,-7,-8,-9,-31,-32,64,-53,-54,-56,92,-28,-29,99,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,64,-27,-26,-30,-43,-10,-11,-12,-13,-14,-15,-50,99,-42,-41,-39,-62,-40,]),'ARROW_LTR':([12,18,20,21,22,23,24,28,29,50,56,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,89,94,95,96,101,102,103,104,105,106,107,108,112,119,120,121,122,131,],[-6,-55,-7,-8,-9,-31,-32,-53,-54,-56,93,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,111,-27,-26,-30,-43,-10,-11,-12,-13,-14,-15,-50,123,-42,-41,-39,-62,-40,]),'RPAREN':([12,18,20,21,22,23,24,28,29,50,59,60,61,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,101,102,103,104,105,106,107,108,119,120,121,122,131,],[-6,-55,-7,-8,-9,-31,-32,-53,-54,-56,-28,-29,96,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,-43,-10,-11,-12,-13,-14,-15,-50,-42,-41,-39,-62,-40,]),'THEN':([12,18,20,21,22,23,24,28,29,50,59,60,62,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,101,102,103,104,105,106,107,108,119,120,121,122,131,],[-6,-55,-7,-8,-9,-31,-32,-53,-54,-56,-28,-29,97,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,-43,-10,-11,-12,-13,-14,-15,-50,-42,-41,-39,-62,-40,]),'ARROW_RTL':([12,18,20,21,22,23,24,28,29,50,59,60,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,94,95,96,101,102,103,104,105,106,107,108,112,119,120,121,122,131,],[-6,-55,-7,-8,-9,-31,-32,-53,-54,-56,-28,-29,-45,-33,-34,-16,-17,-49,-18,-19,-20,-21,-22,-23,-24,-25,-38,-27,-26,-30,-43,-10,-11,-12,-13,-14,-15,-50,125,-42,-41,-39,-62,-40,]),'START':([93,111,],[115,122,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,91,92,97,124,129,137,139,],[1,113,114,116,133,135,141,142,]),'statement':([0,1,91,92,97,113,114,116,124,129,133,135,137,139,141,142,],[2,25,2,2,2,25,25,25,2,2,25,25,2,2,25,25,]),'identifier':([0,1,6,7,8,9,10,11,13,14,15,16,17,19,26,27,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,51,64,77,87,88,90,91,92,94,95,97,99,102,103,104,105,106,107,113,114,116,117,123,124,125,129,133,135,137,139,141,142,],[3,3,50,50,50,54,50,56,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,89,50,50,50,50,50,3,3,50,50,3,50,50,50,50,50,50,50,3,3,3,50,50,3,50,3,3,3,3,3,3,3,]),'expression':([0,1,6,7,8,10,13,14,15,16,17,19,26,27,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,64,77,87,88,90,91,92,94,95,97,99,102,103,104,105,106,107,113,114,116,117,123,124,125,129,133,135,137,139,141,142,],[4,4,49,49,49,55,57,58,59,60,61,62,63,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,100,108,109,110,112,4,4,68,69,4,118,68,69,70,71,72,73,4,4,4,130,132,4,134,4,4,4,4,4,4,4,]),'if_statement':([0,1,91,92,97,113,114,116,124,129,133,135,137,139,141,142,],[5,5,5,5,5,5,5,5,5,136,5,5,5,5,5,5,]),'primitive':([0,1,6,7,8,10,13,14,15,16,17,19,26,27,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,64,77,87,88,90,91,92,94,95,97,99,102,103,104,105,106,107,113,114,116,117,123,124,125,129,133,135,137,139,141,142,],[18,18,18,18,18,18,18,18,18,18,18,18,18,66,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'boolean':([0,1,6,7,8,10,13,14,15,16,17,19,26,27,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,64,77,87,88,90,91,92,94,95,97,99,102,103,104,105,106,107,113,114,116,117,123,124,125,129,133,135,137,139,141,142,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'arguments':([6,7,8,],[48,52,53,]),'assignable':([27,],[65,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_list","S'",1,None,None,None),
  ('statement_list -> statement','statement_list',1,'p_statement_list','tinybits_yacc.py',21),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','tinybits_yacc.py',22),
  ('statement -> identifier','statement',1,'p_statement','tinybits_yacc.py',29),
  ('statement -> expression','statement',1,'p_statement','tinybits_yacc.py',30),
  ('statement -> if_statement','statement',1,'p_statement','tinybits_yacc.py',31),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier','tinybits_yacc.py',38),
  ('primitive -> NUM_INT','primitive',1,'p_primitive','tinybits_yacc.py',44),
  ('primitive -> NUM_FLOAT','primitive',1,'p_primitive','tinybits_yacc.py',45),
  ('primitive -> boolean','primitive',1,'p_primitive','tinybits_yacc.py',46),
  ('expression -> expression PLUS expression PLUS','expression',4,'p_binary_op','tinybits_yacc.py',53),
  ('expression -> expression MINUS expression MINUS','expression',4,'p_binary_op','tinybits_yacc.py',54),
  ('expression -> expression MUL expression MUL','expression',4,'p_binary_op','tinybits_yacc.py',55),
  ('expression -> expression DIV expression DIV','expression',4,'p_binary_op','tinybits_yacc.py',56),
  ('expression -> expression EXP expression EXP','expression',4,'p_binary_op','tinybits_yacc.py',57),
  ('expression -> expression MOD expression MOD','expression',4,'p_binary_op','tinybits_yacc.py',58),
  ('expression -> expression BIT_AND expression','expression',3,'p_binary_op','tinybits_yacc.py',59),
  ('expression -> expression BIT_OR expression','expression',3,'p_binary_op','tinybits_yacc.py',60),
  ('boolean -> expression EQ expression','boolean',3,'p_boolean_operators','tinybits_yacc.py',66),
  ('boolean -> expression NEQ expression','boolean',3,'p_boolean_operators','tinybits_yacc.py',67),
  ('boolean -> expression GT expression','boolean',3,'p_boolean_operators','tinybits_yacc.py',68),
  ('boolean -> expression GTE expression','boolean',3,'p_boolean_operators','tinybits_yacc.py',69),
  ('boolean -> expression LT expression','boolean',3,'p_boolean_operators','tinybits_yacc.py',70),
  ('boolean -> expression LTE expression','boolean',3,'p_boolean_operators','tinybits_yacc.py',71),
  ('boolean -> expression AND expression','boolean',3,'p_boolean_operators','tinybits_yacc.py',72),
  ('boolean -> expression OR expression','boolean',3,'p_boolean_operators','tinybits_yacc.py',73),
  ('expression -> MINUS expression MINUS','expression',3,'p_unary_operation','tinybits_yacc.py',79),
  ('expression -> PLUS expression PLUS','expression',3,'p_unary_operation','tinybits_yacc.py',80),
  ('expression -> BIT_NEG expression','expression',2,'p_unary_operation','tinybits_yacc.py',81),
  ('expression -> NOT expression','expression',2,'p_unary_operation','tinybits_yacc.py',82),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_paren','tinybits_yacc.py',88),
  ('boolean -> TRUE','boolean',1,'p_boolean','tinybits_yacc.py',94),
  ('boolean -> FALSE','boolean',1,'p_boolean','tinybits_yacc.py',95),
  ('assignable -> primitive','assignable',1,'p_assignable','tinybits_yacc.py',101),
  ('assignable -> expression','assignable',1,'p_assignable','tinybits_yacc.py',102),
  ('arguments -> arguments COMMA expression','arguments',3,'p_comma_separated_expr','tinybits_yacc.py',108),
  ('arguments -> expression','arguments',1,'p_comma_separated_expr','tinybits_yacc.py',109),
  ('arguments -> <empty>','arguments',0,'p_comma_separated_expr','tinybits_yacc.py',110),
  ('expression -> LSQBRACK arguments RSQBRACK','expression',3,'p_arrays','tinybits_yacc.py',117),
  ('expression -> identifier LSQBRACK expression RSQBRACK','expression',4,'p_array_access','tinybits_yacc.py',123),
  ('expression -> identifier LSQBRACK expression COLON expression RSQBRACK','expression',6,'p_slice','tinybits_yacc.py',129),
  ('expression -> identifier LSQBRACK COLON expression RSQBRACK','expression',5,'p_slice','tinybits_yacc.py',130),
  ('expression -> identifier LSQBRACK expression COLON RSQBRACK','expression',5,'p_slice','tinybits_yacc.py',131),
  ('expression -> identifier LSQBRACK COLON RSQBRACK','expression',4,'p_slice','tinybits_yacc.py',132),
  ('statement -> identifier LSQBRACK expression RSQBRACK EQUALS expression','statement',6,'p_array_access_assign','tinybits_yacc.py',139),
  ('expression -> identifier EQUALS assignable','expression',3,'p_assign','tinybits_yacc.py',145),
  ('if_statement -> IF expression THEN statement_list END','if_statement',5,'p_ifstatement','tinybits_yacc.py',151),
  ('if_statement -> IF expression THEN statement_list ELSE statement_list END','if_statement',7,'p_ifstatement_else','tinybits_yacc.py',157),
  ('if_statement -> IF expression THEN statement_list ELSE if_statement','if_statement',6,'p_ifstatement_else_if_else','tinybits_yacc.py',163),
  ('expression -> expression IN expression','expression',3,'p_in_expression','tinybits_yacc.py',169),
  ('expression -> expression NOT IN expression','expression',4,'p_in_expression','tinybits_yacc.py',170),
  ('statement -> SETOUT arguments','statement',2,'p_SETOUT_statement','tinybits_yacc.py',176),
  ('statement -> GETIN arguments','statement',2,'p_GETIN_statement','tinybits_yacc.py',182),
  ('expression -> identifier DOUBLE_PLUS','expression',2,'p_increment_decrement_identifiers','tinybits_yacc.py',189),
  ('expression -> identifier DOUBLE_MINUS','expression',2,'p_increment_decrement_identifiers','tinybits_yacc.py',190),
  ('expression -> primitive','expression',1,'p_expression','tinybits_yacc.py',196),
  ('expression -> identifier','expression',1,'p_expression','tinybits_yacc.py',197),
  ('statement -> FOR identifier IN expression ARROW_LTR expression DO statement_list LOOP','statement',9,'p_for_loop','tinybits_yacc.py',203),
  ('statement -> FOR identifier IN expression ARROW_RTL expression DO statement_list LOOP','statement',9,'p_for_loop','tinybits_yacc.py',204),
  ('statement -> FOR identifier IN expression DO statement_list LOOP','statement',7,'p_for_in_loop','tinybits_yacc.py',210),
  ('statement -> WHILE expression DO statement_list LOOP','statement',5,'p_while_loop','tinybits_yacc.py',216),
  ('statement -> PROCCES identifier COLON statement_list END','statement',5,'p_procces_declaration','tinybits_yacc.py',223),
  ('expression -> PROCCES identifier ARROW_LTR START','expression',4,'p_procces_call','tinybits_yacc.py',230),
  ('statement -> PROCCES identifier ARROW_LTR START','statement',4,'p_procces_call','tinybits_yacc.py',231),
]

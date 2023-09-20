grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// keywords
BREAK: 'break';

CONTINUE: 'continue';

IF: 'if';

ELSE: 'else';

FOR: 'for';

// TRUE: 'true';

// FALSE: 'false';

INT: 'int';

FLOAT: 'float';

BOOL: 'bool';

STRING: 'string';

RETURN: 'return';

NULL: 'null';

CLASS: 'class';

CONSTRUCTOR: 'constructor';

VAR: 'var';

SELF: 'self';

NEW: 'new';

VOID: 'void';

CONST: 'const';

FUNC: 'func';

// Operators
ADD_OP: '+';

SUB_OP: '-';

MUL_OP: '*';

SLASH: '/';

BACKSLASH: '\\';

NOT_OP: '!';

AND_OP: '&&';

OR_OP: '||';

EQUAL_OP: '==';

ASSIGN_OP: ':=';

DECL_OP: '=';

DIFF_OP: '!=';

LESS_OP: '<';

LESS_EQUAL_OP: '<=';

GREATER_OP: '>';

GREATER_EQUAL_OP: '>=';

CONCAT_OP: '^';

MOD_OP: '%';

LP: '(';

RP: ')';

LSB: '[';

RSB: ']';

DOT: '.';

COMMA: ',';

COLON: ':';

SEMICOLON: ';';

LCB: '{';

RCB: '}';

SIN_Q: '\'';

DOU_Q: '"';

// main program
program: (exp | stmt | decl)+ EOF; 

// expressions (priority from low to high)
exp: exp (ADD_OP | SUB_OP) exp1 | exp1;
exp1: exp1 (MUL_OP | BACKSLASH | SLASH | MOD_OP) exp2 | exp2;
exp2: exp2 (EQUAL_OP | DIFF_OP | GREATER_OP | GREATER_EQUAL_OP | LESS_EQUAL_OP | LESS_OP) exp3 | exp3;
exp3: exp3 (AND_OP | OR_OP) exp4 | exp4;
exp4: NOT_OP exp5 | exp5;
exp5: SUB_OP exp6 |exp6;
exp6: exp7 (CONCAT_OP) exp7 | exp7;
exp7: literal | LP (exp) RP | ID | arr_ele | obj_exp;

literal: INT_LIT | FLOAT_LIT | STR_LIT | BOOL_LIT | array_lit;

exp_list: exp (COMMA exp)*;

ref_type: value_type | array_type;

value_type: INT | FLOAT | STRING | BOOL;
array_type: LSB INT_LIT RSB value_type;

func_type: ref_type | VOID;

// declaration
decl: class_decl | attr_decl | method_decl;

class_decl: CLASS ID ('<-' ID)? LCB (stmt | decl)* RCB;

obj_exp: NEW ID LP RP; 

// method declaration
method_decl: func_decl | constructor_decl | static_func_decl | static_constructor_decl;

// replace Int by type
func_decl: FUNC ID expo_func;
static_func_decl: FUNC AT_ID expo_func;
expo_func: LP params_list? RP COLON func_type block_stmt;

constructor_decl: FUNC ID expo_constructor;
static_constructor_decl: FUNC AT_ID expo_constructor;
expo_constructor: LP params_list? RP block_stmt;


// attribute declaration
attr_decl: (VAR | CONST) attr_decl_body SEMICOLON;

attr_decl_body: attr_decl_body_full | attr_decl_body_short;

// replace INT_LIT with exp
// replace INT with type
attr_decl_body_short: ID (COMMA ID)* COLON ref_type;
attr_decl_body_full: 
	ID COMMA attr_decl_body_full COMMA exp
	| ID COLON ref_type DECL_OP exp;

// statements
stmt: assign_stmt;

assign_stmt: ID ASSIGN_OP exp SEMICOLON;

block_stmt: LCB body RCB;

body: stmt body | decl body | ;

// replace INT with type
params_list: param (COMMA param)* | params_same_type;
param: ID COLON ref_type;
params_same_type: ID (COMMA ID)* COLON ref_type;

arr_ele: ID LSB INT_LIT RSB;

// Literals
array_lit: LSB exp_list RSB;

FLOAT_LIT: INT_LIT DECPART | INT_LIT DECPART? EXPPART;
fragment DECPART: DOT [0-9]*;
fragment EXPPART: [eE] [+-]? INT_LIT;

INT_LIT: ([0-9]+) { 
	while self.text[0] == '0':
		self.text = self.text[1:]
};

STR_LIT: (DOU_Q (~["] | BACKSLASH DOU_Q)* DOU_Q) {
	self.text = self.text[1:-1]
};

BOOL_LIT: 'true' | 'false';

// ARR_LIT: LSB (exp (COMMA exp)*)? RSB;

// Identifiers
ID: [a-zA-Z_] SEQUENCE*;
AT_ID: '@' SEQUENCE+;
fragment SEQUENCE: [a-zA-Z0-9_];

// COMMENT: ([/] [*]) ([]*?) ([*] [/])
CMT_LINE: '//' ~[\r\n]* -> skip;
CMT_BLOCK: '/*' .*? '*/' -> skip;


WS: [ \t\r\n\f\b]+ -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
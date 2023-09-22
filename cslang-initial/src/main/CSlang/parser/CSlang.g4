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

DIV_OP: '/';

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
exp: exp1 CONCAT_OP exp1 | exp1;
exp1:
	exp2 (
		EQUAL_OP
		| DIFF_OP
		| GREATER_OP
		| GREATER_EQUAL_OP
		| LESS_EQUAL_OP
		| LESS_OP
	) exp2
	| exp2;
exp2: exp2 (AND_OP | OR_OP) exp3 | exp3;
exp3: exp3 (ADD_OP | SUB_OP) exp4 | exp4;
exp4: exp4 (MUL_OP | DIV_OP | '\\' | MOD_OP) exp5 | exp5;
exp5: NOT_OP exp5 | exp6;
exp6: SUB_OP exp6 | exp7;
exp7: arr_ele | exp8;
exp8: inst_access | static_access | exp9;
exp9: obj_cre | literal | LP (exp) RP | ID | func_call;

literal: INT_LIT | FLOAT_LIT | STR_LIT | BOOL_LIT | array_lit;

exp_list: exp (COMMA exp)*;

// types
func_type: ref_type | VOID;

ref_type: value_type | array_type;

value_type: INT | FLOAT | STRING | BOOL;

array_type: LSB INT_LIT RSB value_type;

// declarations
decl: class_decl | attr_decl | method_decl;

// class declarations
class_decl: CLASS (ID '<-')? ID LCB (stmt | decl)* RCB;

static_access: static_mem_access | static_method_access;

inst_access: mem_access | method_access;

obj_cre: NEW ID LP exp_list? RP;

mem_access: (exp9 | SELF) DOT ID;

static_mem_access: (ID DOT)? AT_ID;

method_access: (exp9 | SELF) DOT ID LP exp_list? RP;

static_method_access: (ID DOT)? AT_ID LP exp_list? RP;

// method declarations
method_decl:
	func_decl
	| constructor_decl
	| static_func_decl
	| static_constructor_decl;

func_decl: FUNC ID expo_func;
static_func_decl: FUNC AT_ID expo_func;
expo_func: LP params_list? RP COLON func_type block_stmt;

constructor_decl: FUNC ID expo_constructor;
static_constructor_decl: FUNC AT_ID expo_constructor;
expo_constructor: LP params_list? RP block_stmt;

func_call: (ID | AT_ID) LP exp_list? RP;

// attribute declarations 
attr_decl: (VAR | CONST) attr_decl_body SEMICOLON;
attr_decl_body: attr_decl_body_full | attr_decl_body_short;
attr_decl_body_short: (ID | AT_ID) (COMMA (ID | AT_ID))* COLON ref_type;
attr_decl_body_full:
	(ID | AT_ID) COMMA attr_decl_body_full COMMA exp
	| (ID | AT_ID) COLON ref_type DECL_OP exp;

// statements
stmt:
	assign_stmt SEMICOLON
	| if_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| method_invocation_stmt;

assign_stmt: exp ASSIGN_OP exp;

if_stmt: IF block_stmt? exp block_stmt (ELSE block_stmt)?;

for_stmt:
	FOR assign_stmt SEMICOLON exp SEMICOLON assign_stmt block_stmt;

break_stmt: BREAK SEMICOLON;

continue_stmt: CONTINUE SEMICOLON;

return_stmt: RETURN exp? SEMICOLON;

method_invocation_stmt: (method_access | static_method_access) SEMICOLON;

block_stmt: LCB body RCB;

// body: stmt body | decl body |;
body: (stmt | decl)*;

params_list: params_1_type (COMMA params_1_type)*;
params_1_type: ID (COMMA ID)* COLON ref_type;

// Literals
array_lit: LSB exp_list? RSB;

arr_ele: ID LSB exp8 RSB;

FLOAT_LIT: INT_LIT DECPART | INT_LIT DECPART? EXPPART;
fragment DECPART: DOT [0-9]*;
fragment EXPPART: [eE] [+-]? INT_LIT;

INT_LIT: ([0-9]+);

STR_LIT:
	DOU_Q (~["\\] | ESCAPE)* DOU_Q {
	self.text = self.text[1:-1]
};
fragment NEWLINE: '\r'? '\n';
fragment ESCAPE:
	'\\b'
	| '\\f'
	| '\\r'
	| '\\n'
	| '\\t'
	| '\\"'
	| '\\\\';

BOOL_LIT: 'true' | 'false';

// Identifiers
ID: [a-zA-Z_] SEQUENCE*;
AT_ID: '@' SEQUENCE+;
fragment SEQUENCE: [a-zA-Z0-9_];

// COMMENT
CMT_LINE: '//' ~[\r\n]* -> skip;
CMT_BLOCK: '/*' .*? '*/' -> skip;

WS: [ \t\r\n\f\b]+ -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};

ILLEGAL_ESCAPE:
	DOU_Q (~["] | '\\"')* DOU_Q {
	esc_list = ['b', 'f', 'r', 'n', 't', '"', '\\']
	for idx in range(1, len(self.text) - 2):
		if self.text[idx] == '\\' and self.text[idx+1] not in esc_list:
			raise IllegalEscape(self.text[1:-1]) 
			break
};

UNCLOSE_STRING:
	DOU_Q (~["] | ESCAPE)*? (NEWLINE | EOF) {
	string_error = self.text[1:]
	if (string_error[-1] == "\n"):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
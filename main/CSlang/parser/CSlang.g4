grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// keywords PROGRAM_CLASS: 'Program';

// MAIN: '@main';

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

DOU_Q: '"';

INHERIT: '<-';

// main program
program: prog_decl_list EOF;

// program can null-able???
prog_decl_list: prog_decl prog_decl_list | prog_decl;

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
exp8: exp8 DOT ID | exp8 DOT ID LP exp_list RP | exp9;
exp9: static_access | exp10;
exp10:
	obj_cre
	| literal
	| LP (exp) RP
	| ID
	| self_access
	| NULL;

literal: ele_literal | array_lit;
ele_literal: INT_LIT | FLOAT_LIT | STR_LIT | BOOL_LIT;
ele_literal_list:
	ele_literal COMMA ele_literal_list
	| ele_literal;

exp_list: exp_prime |;
exp_prime: exp COMMA exp_prime | exp;

// types
func_type: ref_type | VOID;

ref_type: ele_type | array_type;

array_type: LSB INT_LIT RSB ele_type;

ele_type: value_type | ID;

value_type: INT | FLOAT | STRING | BOOL;

// declarations prog_decl: class_decl | program_class_decl;
prog_decl: class_decl;

// class declarations
class_decl:
	CLASS ID INHERIT ID LCB class_mem_list RCB
	| CLASS ID LCB class_mem_list RCB;
// program_class_decl: CLASS PROGRAM_CLASS LCB prog_class_mem_list RCB;

class_mem_list: class_mem class_mem_list |;
class_mem: attr_decl | method_decl;

// prog_class_mem_list: prog_class_mem prog_class_mem_list |; prog_class_mem: class_mem |
// main_func_decl;

obj_cre: NEW ID LP exp_list RP;

// inst_mem_access: exp8 DOT ID;
inst_method_access: exp8 DOT ID LP exp_list RP;

static_access: static_mem_access | static_method_access;
static_mem_access: (ID DOT)? AT_ID;
static_method_access: (ID DOT)? AT_ID LP exp_list RP;

self_access: self_mem_access | self_method_access;
self_mem_access: SELF DOT (ID | AT_ID);
self_method_access: SELF DOT (ID | AT_ID) LP exp_list RP;

// method declarations
method_decl: func_decl | constructor_decl | static_func_decl;

func_decl: FUNC ID expo_func;
static_func_decl: FUNC AT_ID expo_func;
expo_func: LP params_list RP COLON func_type block_stmt;

// main_func_decl: FUNC MAIN LP RP COLON (VOID | INT) block_stmt;

constructor_decl: FUNC CONSTRUCTOR LP params_list RP block_stmt;

// attribute declarations 
attr_decl: const_decl | var_decl;
const_decl: CONST attr_decl_body SEMICOLON;
var_decl: VAR attr_decl_body SEMICOLON;
attr_decl_body: attr_decl_body_full | attr_decl_body_short;
attr_decl_body_short: identifier_list COLON ref_type;

attr_decl_body_full:
	(ID | AT_ID) COMMA attr_decl_body_full COMMA exp
	| (ID | AT_ID) COLON ref_type DECL_OP exp;

identifier_list: (ID | AT_ID) COMMA identifier_list
	| (ID | AT_ID);

// statements
stmt:
	assign_stmt SEMICOLON
	| if_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| method_invocation_stmt
	| decl_stmt;

decl_stmt: const_decl_stmt | var_decl_stmt;
const_decl_stmt: CONST decl_stmt_body SEMICOLON;
var_decl_stmt: VAR decl_stmt_body SEMICOLON;
decl_stmt_body: decl_stmt_body_short | decl_stmt_body_full;
decl_stmt_body_short: id_list_not_null COLON ref_type;
decl_stmt_body_full:
	ID COMMA decl_stmt_body_full COMMA exp
	| ID COLON ref_type DECL_OP exp;


assign_stmt: exp7 ASSIGN_OP exp;

if_stmt: IF block_stmt? exp block_stmt (ELSE block_stmt)?;

for_stmt:
	FOR assign_stmt SEMICOLON exp SEMICOLON assign_stmt block_stmt;

break_stmt: BREAK SEMICOLON;

continue_stmt: CONTINUE SEMICOLON;

return_stmt: RETURN exp? SEMICOLON;

method_invocation_stmt: (
		inst_method_access
		| static_method_access
		| self_method_access
	) SEMICOLON;

block_stmt: LCB body RCB;

body: stmt body |;

params_list: params_prime |;
params_prime: params_1_type COMMA params_prime | params_1_type;
params_1_type: id_list_not_null COLON ref_type;

id_list_not_null: ID COMMA id_list_not_null | ID;

// Literals
array_lit: LSB ele_literal_list RSB;

arr_ele: exp8 LSB exp RSB;

FLOAT_LIT: INT_LIT DECPART | INT_LIT DECPART? EXPPART;
fragment DECPART: DOT [0-9]*;
fragment EXPPART: [eE] [+-]? INT_LIT;

INT_LIT: ([0-9]+) {
	for i in self.text:
		if i != '0' or self.text == '0':
			break
		self.text = self.text[1:] 
};

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
	| '\\\\'
	| '\\"';

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

ILLEGAL_ESCAPE:
	DOU_Q (~["] | '\\"')* DOU_Q {
	esc_list = ['b', 'f', 'r', 'n', 't', '"', '\\']
	for idx in range(1, len(self.text) - 2):
		if self.text[idx] == '\\' and self.text[idx+1] not in esc_list:
			raise IllegalEscape(self.text[1:idx + 2]) 
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

ERROR_CHAR: . {raise ErrorToken(self.text)};
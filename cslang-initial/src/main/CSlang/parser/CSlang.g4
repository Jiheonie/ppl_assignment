grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

// expressions
exp: exp1 (MUL_OP | PLUS_OP) exp1 | exp1;

exp1: INT_LIT | FLOAT_LIT;

// declarations by BNF 
// (not EBNF -> decl+)
decllist: decl decllist | decl;

decl: class_decl | attr_decl;

class_decl: CLASS ID ('<-' ID)? LCB (attr_decl)* RCB;

attr_decl:
	(VAR | CONST) ID (COMMA ID)* COLON INT (ASSIGN_OP exp)? SEMICOLON;

attr_decl1: ID EQUAL_OP INT_LIT;

// statements
assign_stmt: ID exp SEMICOLON;

// Literals
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

BOOL_LIT: TRUE | FALSE;

// ARR_LIT: LSB (exp (COMMA exp)*)? RSB;

// Identifiers
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

// COMMENT: ([/] [*]) ([]*?) ([*] [/])
CMT_LINE: '//' ~[\r\n]* -> skip;

// keywords
BREAK: 'break';

CONTINUE: 'continue';

IF: 'if';

ELSE: 'else';

FOR: 'for';

TRUE: 'true';

FALSE: 'false';

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
PLUS_OP: '+';

MINUS_OP: '-';

MUL_OP: '*';

SLASH: '/';

BACKSLASH: '\\';

NOT_OP: '!';

AND_OP: '&&';

OR_OP: '||';

EQUAL_OP: '==';

ASSIGN_OP: ':=';

// ASSIGN_OP: '=';

DIFF_OP: '!=';

LESS_OP: '<';

LESS_EQUAL_OP: '<=';

GREATER_OP: '>';

GREATER_EQUAL_OP: '>=';

CONCAT_OP: '^';

DIV_OP: '%';

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

WS: [ \t\r\n\f\b]+ -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
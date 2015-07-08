grammar oftexmath;

/** The start rule; begin parsing here. */
init       : main+ ;

main       : mainexpr+ | allinone+;

allinone        : braceoc //+ (variable | number | expr)*
           | variable //+ (number | expr)*
           | number //+ (variable | expr)*
           | expr //+ (variable | number)*
           | muldiv
           | signs
           | colformat
           | rowdelimit
           ;

braceoc    : BRACEOPEN (braceoc | muldiv | variable | number | signs)+ BRACECLOSE ;

signs      : PLUS | MINUS | EQ ;

muldiv     : mul | div ;

mul        : variable MUL (braceoc | number | expr | variable | div | mul)
           | number MUL (braceoc | expr | variable | number | div | mul)
           | expr MUL (braceoc | variable | number | expr | div | mul)
           ;

div        : variable DIV (braceoc | number | expr | variable | div | mul)
           | number DIV (braceoc | expr | variable | number | div | mul)
           | expr DIV (braceoc | variable | number | expr | div | mul)
           ;

colformat  : COLFORMAT ;

rowdelimit : ROWDELIMIT ;

variable   : VARIABLE
           | VARIABLE subset
           | VARIABLE superset
           | VARIABLE subset superset
           ;

number     : NUMBER
           | NUMBER subset
           | NUMBER superset
           | NUMBER subset superset
           ;

subset     : SUBSET (VARIABLE | NUMBER)
           | SUBSET LEFTBRACE (braceoc | variable | number | expr | muldiv | signs)+ RIGHTBRACE
           ;

superset   : SUPERSET (VARIABLE | NUMBER)
           | SUPERSET LEFTBRACE (braceoc | variable | number | expr | muldiv | signs)+ RIGHTBRACE
           ;

mainexpr   : BACKSLASH mainwords LEFTBRACE subwords RIGHTBRACE ;

expr       : BACKSLASH keywords (subset | superset)?
           | BACKSLASH keywords subset? superset
           | BACKSLASH keywords LEFTBRACE (braceoc | variable | number | expr | muldiv | signs)* RIGHTBRACE (subset | superset)?
           | BACKSLASH keywords LEFTBRACE (braceoc | variable | number | expr | muldiv | signs)* RIGHTBRACE subset? superset
           | BACKSLASH keywords LEFTBRACE (braceoc | variable | number | expr | muldiv | signs)* RIGHTBRACE LEFTBRACE (braceoc | variable | number | expr | muldiv | signs)* RIGHTBRACE (subset | superset)?
           | BACKSLASH keywords LEFTBRACE (braceoc | variable | number | expr | muldiv | signs)* RIGHTBRACE LEFTBRACE (braceoc | variable | number | expr | muldiv | signs)* RIGHTBRACE subset? superset
           ;

mainwords  : MAINWORDS ;

subwords   : SUBWORDS ;

keywords   : KEYWORDS ;

VARIABLE   : [a-zA-Z]{1} ;
NUMBER     : [0-9] ;
BACKSLASH  : '\\' ;
SUBSET     : '_' ;
SUPERSET   : '^' ;
LEFTBRACE  : '{' ;
RIGHTBRACE : '}' ;
COLFORMAT  : '&' ;
BRACEOPEN  : '(' ;
BRACECLOSE : ')' ;
EQ         : '=' ;
PLUS       : '+' ;
MINUS      : '-' ;
MUL        : '*' ;
DIV        : '/' ;
ROWDELIMIT : '\\\\' ;

MAINWORDS  : 'begin' | 'end' ;

SUBWORDS   : 'math' | 'array' ;

KEYWORDS   : 'mathbf' | 'mathit' | 'boldsymbol' | 'sum' | 'int' | 'frac' ;

WS         : [ \t\r\n]+ -> skip ;
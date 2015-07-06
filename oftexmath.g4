grammar oftexmath;

/** The start rule; begin parsing here. */
init       : main+ ;

main       : mainexpr (allinone | mainexpr)* | mainexpr (allinone | mainexpr)* mainexpr | allinone;

allinone        : braceoc+ (variable | number | expr)*
           | variable+ (number | expr)*
           | number+ (variable | expr)*
           | expr+ (variable | number)*
           | muldiv
           | signs
           | colformat{0,1}
           | rowdelimit{0,1}
           ;

braceoc    : BRACEOPEN (allinone)* BRACECLOSE ;

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
           | SUBSET LEFTBRACE allinone RIGHTBRACE
           ;

superset   : SUPERSET (VARIABLE | NUMBER)
           | SUPERSET LEFTBRACE allinone RIGHTBRACE
           ;

mainexpr   : BACKSLASH mainwords LEFTBRACE subwords{0,1} RIGHTBRACE ;

expr       : BACKSLASH keywords
           | BACKSLASH keywords
           | BACKSLASH keywords LEFTBRACE allinone RIGHTBRACE
           | BACKSLASH keywords subset
           | BACKSLASH keywords LEFTBRACE allinone RIGHTBRACE subset
           | BACKSLASH keywords superset
           | BACKSLASH keywords LEFTBRACE allinone RIGHTBRACE superset
           | BACKSLASH keywords subset superset
           | BACKSLASH keywords LEFTBRACE allinone RIGHTBRACE subset superset
           | BACKSLASH keywords LEFTBRACE allinone RIGHTBRACE LEFTBRACE allinone RIGHTBRACE
           | BACKSLASH keywords LEFTBRACE allinone RIGHTBRACE LEFTBRACE allinone RIGHTBRACE subset
           | BACKSLASH keywords LEFTBRACE allinone RIGHTBRACE LEFTBRACE allinone RIGHTBRACE superset
           | BACKSLASH keywords LEFTBRACE allinone RIGHTBRACE LEFTBRACE allinone RIGHTBRACE subset superset
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

KEYWORDS   : 'mathbf' | 'sum' | 'frac' ;

WS         : [ \t\r\n]+ -> skip ;
%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1 
%}

%token ARRAY
%token MAP
%token CONST_AC_MOD
%token DO
%token ELSE
%token IF
%token INT
%token ELIF
%token WHILE
%token FOR
%token RANGE
%token CLASS
%token STRUCT
%token STRING
%token FLOAT
%token CHAR
%token BOOLEAN
%token READ
%token WRITE
%token EMOJI_PRINT
%token RETURN
%token FUN
%token KEY
%token VALUE
%token MAIN
%token ENTRY
%token EMOJI_ENTRY_POINT

%token ID
%token CONST

%token COLON
%token SEMICOLON
%token COMMA
%token PERIOD
%token CURLY_LEFT
%token CURLY_RIGHT
%token ROUND_LEFT
%token ROUND_RIGHT
%token SQUARE_LEFT
%token SQUARE_RIGHT

%token PLUS
%token MINUS
%token MUL
%token DIV
%token LESS
%token GREATER
%token LESS_EQ
%token GREATER_EQ
%token NOT_EQ
%token BOOL_EQ
%token EQUAL        /* for assign */
%token EXCLAM
%token QUESTION
%token STRING_EQ
%token AND
%token OR

%start program 

%%
program : ENTRY cmpstmt | EMOJI_ENTRY_POINT cmpstmt;
declaration : type ID;
type : STRING | FLOAT | CHAR | BOOLEAN | INT;
/* array : None | ARRAY SQUARE_LEFT CONST SQUARE_RIGHT; */
cmpstmt : CURLY_LEFT stmtlist CURLY_RIGHT;
stmtlist : stmt stmtTemp;
stmtTemp : /*None*/ | stmtlist;
stmt : simplestmt SEMICOLON | structstmt;
simplestmt : assignstmt | iostmt | declaration;
structstmt : cmpstmt | ifstmt | whilestmt | forstmt;
ifstmt : IF ROUND_LEFT boolean_condition ROUND_RIGHT cmpstmt tempIf;
tempIf : /*None*/ | ELSE cmpstmt;
forstmt : FOR forheader cmpstmt;
forheader : ROUND_LEFT INT assignstmt SEMICOLON boolean_condition SEMICOLON assignstmt ROUND_RIGHT;
whilestmt : WHILE ROUND_LEFT boolean_condition ROUND_RIGHT cmpstmt;
assignstmt : ID EQUAL expression;
expression : term2 term1;
term1 : MUL term2 term1 | DIV term2 term1 | /*None*/
term2 : ROUND_LEFT expression ROUND_RIGHT | CONST | ID | index ;
index : ID SQUARE_LEFT CONST SQUARE_RIGHT ;
iostmt : READ ROUND_LEFT STRING ROUND_RIGHT | WRITE ROUND_LEFT STRING ROUND_RIGHT | EMOJI_PRINT ROUND_LEFT ID ROUND_RIGHT;
condition :     expression GREATER expression |
                expression GREATER_EQ expression |
                expression LESS expression |
                expression LESS_EQ expression |
                expression BOOL_EQ expression |
                expression NOT_EQ expression |
                expression STRING_EQ expression;
boolean_condition : condition bool_condition_temp;
bool_condition_temp : /*None*/ | AND boolean_condition | OR boolean_condition ;
%%
yyerror(char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}
/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    ARRAY = 258,
    MAP = 259,
    CONST_AC_MOD = 260,
    DO = 261,
    ELSE = 262,
    IF = 263,
    INT = 264,
    NUMBER = 265,
    ELIF = 266,
    WHILE = 267,
    FOR = 268,
    RANGE = 269,
    CLASS = 270,
    STRUCT = 271,
    STRING = 272,
    FLOAT = 273,
    CHAR = 274,
    BOOLEAN = 275,
    READ = 276,
    WRITE = 277,
    EMOJI_PRINT = 278,
    RETURN = 279,
    FUN = 280,
    KEY = 281,
    VALUE = 282,
    MAIN = 283,
    ENTRY = 284,
    EMOJI_ENTRY_POINT = 285,
    ID = 286,
    CONST = 287,
    COLON = 288,
    SEMICOLON = 289,
    COMMA = 290,
    PERIOD = 291,
    CURLY_LEFT = 292,
    CURLY_RIGHT = 293,
    ROUND_LEFT = 294,
    ROUND_RIGHT = 295,
    SQUARE_LEFT = 296,
    SQUARE_RIGHT = 297,
    PLUS = 298,
    MINUS = 299,
    MUL = 300,
    DIV = 301,
    LESS = 302,
    GREATER = 303,
    LESS_EQ = 304,
    GREATER_EQ = 305,
    NOT_EQ = 306,
    BOOL_EQ = 307,
    EQUAL = 308,
    EXCLAM = 309,
    QUESTION = 310,
    STRING_EQ = 311,
    AND = 312,
    OR = 313
  };
#endif
/* Tokens.  */
#define ARRAY 258
#define MAP 259
#define CONST_AC_MOD 260
#define DO 261
#define ELSE 262
#define IF 263
#define INT 264
#define NUMBER 265
#define ELIF 266
#define WHILE 267
#define FOR 268
#define RANGE 269
#define CLASS 270
#define STRUCT 271
#define STRING 272
#define FLOAT 273
#define CHAR 274
#define BOOLEAN 275
#define READ 276
#define WRITE 277
#define EMOJI_PRINT 278
#define RETURN 279
#define FUN 280
#define KEY 281
#define VALUE 282
#define MAIN 283
#define ENTRY 284
#define EMOJI_ENTRY_POINT 285
#define ID 286
#define CONST 287
#define COLON 288
#define SEMICOLON 289
#define COMMA 290
#define PERIOD 291
#define CURLY_LEFT 292
#define CURLY_RIGHT 293
#define ROUND_LEFT 294
#define ROUND_RIGHT 295
#define SQUARE_LEFT 296
#define SQUARE_RIGHT 297
#define PLUS 298
#define MINUS 299
#define MUL 300
#define DIV 301
#define LESS 302
#define GREATER 303
#define LESS_EQ 304
#define GREATER_EQ 305
#define NOT_EQ 306
#define BOOL_EQ 307
#define EQUAL 308
#define EXCLAM 309
#define QUESTION 310
#define STRING_EQ 311
#define AND 312
#define OR 313

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */

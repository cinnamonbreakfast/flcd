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
    ELIF = 265,
    WHILE = 266,
    FOR = 267,
    RANGE = 268,
    CLASS = 269,
    STRUCT = 270,
    STRING = 271,
    FLOAT = 272,
    CHAR = 273,
    BOOLEAN = 274,
    READ = 275,
    WRITE = 276,
    EMOJI_PRINT = 277,
    RETURN = 278,
    FUN = 279,
    KEY = 280,
    VALUE = 281,
    MAIN = 282,
    ENTRY = 283,
    EMOJI_ENTRY_POINT = 284,
    ID = 285,
    CONST = 286,
    COLON = 287,
    SEMICOLON = 288,
    COMMA = 289,
    PERIOD = 290,
    CURLY_LEFT = 291,
    CURLY_RIGHT = 292,
    ROUND_LEFT = 293,
    ROUND_RIGHT = 294,
    SQUARE_LEFT = 295,
    SQUARE_RIGHT = 296,
    PLUS = 297,
    MINUS = 298,
    MUL = 299,
    DIV = 300,
    LESS = 301,
    GREATER = 302,
    LESS_EQ = 303,
    GREATER_EQ = 304,
    NOT_EQ = 305,
    BOOL_EQ = 306,
    EQUAL = 307,
    EXCLAM = 308,
    QUESTION = 309,
    STRING_EQ = 310,
    AND = 311,
    OR = 312
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
#define ELIF 265
#define WHILE 266
#define FOR 267
#define RANGE 268
#define CLASS 269
#define STRUCT 270
#define STRING 271
#define FLOAT 272
#define CHAR 273
#define BOOLEAN 274
#define READ 275
#define WRITE 276
#define EMOJI_PRINT 277
#define RETURN 278
#define FUN 279
#define KEY 280
#define VALUE 281
#define MAIN 282
#define ENTRY 283
#define EMOJI_ENTRY_POINT 284
#define ID 285
#define CONST 286
#define COLON 287
#define SEMICOLON 288
#define COMMA 289
#define PERIOD 290
#define CURLY_LEFT 291
#define CURLY_RIGHT 292
#define ROUND_LEFT 293
#define ROUND_RIGHT 294
#define SQUARE_LEFT 295
#define SQUARE_RIGHT 296
#define PLUS 297
#define MINUS 298
#define MUL 299
#define DIV 300
#define LESS 301
#define GREATER 302
#define LESS_EQ 303
#define GREATER_EQ 304
#define NOT_EQ 305
#define BOOL_EQ 306
#define EQUAL 307
#define EXCLAM 308
#define QUESTION 309
#define STRING_EQ 310
#define AND 311
#define OR 312

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */

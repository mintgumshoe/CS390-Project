File Descriptions:

--------------------------------------------------------------
tokens.py
--------------------------------------------------------------

Defines the TokenType enum, Token dataclass, and keyword mappings.

Purpose:

Describes every token (PLUS, MINUS, LET, PRINT, NUMBER, ID, etc.)

Provides the Token object used by both the lexer and parser

Stores which words are keywords (let, print)

What it contains:

TokenType class — constants representing all token kinds

Token dataclass — stores type, value, and position

KEYWORDS dictionary — maps identifiers → keyword tokens

--------------------------------------------------------------
lexer.py
--------------------------------------------------------------

Implements the Lexer, also known as the Tokenizer.

Purpose:

The lexer reads raw text and converts it into a stream of tokens the parser can understand.

Responsibilities:

Reads characters one by one

Groups them into meaningful units:

numbers

identifiers

keywords (let, print)

operators (+, -, *, /)

symbols (=, (, ), ;)

Skips whitespace

Raises errors for invalid characters

Output:

A sequence like:

LET, ID(x), ASSIGN, NUMBER(10), PLUS, NUMBER(5), SEMI

----------------------------------------------------------------
ast_nodes.py
----------------------------------------------------------------

Defines classes representing the Abstract Syntax Tree (AST).

Purpose:

After parsing, the program becomes a tree of Python objects.

Contains these node types:

Program(statements)

Assign(name, expr)

Print(expr)

BinOp(left, op, right)

UnaryOp(op, expr)

Num(value)

Var(name)

Example:

Code:

let x = 10 + 5;


AST:

Assign(
    name="x",
    expr=BinOp(
        left=Num(10),
        op=PLUS,
        right=Num(5)
    )
)

-------------------------------------------------------------
parser.py
-------------------------------------------------------------

Implements a recursive descent parser that reads tokens and builds the AST.

Purpose:

Transform the token stream from the lexer into a structured tree.

Responsibilities:

Validate grammar rules

Order of operations (* and / before + and -)

Parse statements:

variable assignments

print calls

Parse expressions:

arithmetic

parenthesis

variable references

Grammar Implemented:
program      → statement_list EOF
statement    → let ID = expr
             | print(expr)
statement_list → (statement ";")+
expr         → term (("+"|"-") term)*
term         → factor (("*"|"/") factor)*
factor       → NUMBER
             | ID
             | "(" expr ")"
             | ("+"|"-") factor

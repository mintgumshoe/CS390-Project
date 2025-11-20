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

operators (+, -, *, /, <, >, %)

symbols (=, (, ), ", ;)

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

Str(value)

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
             | STRING
             | "(" expr ")"
             | ("+"|"-") factor

-------------------------------------------------------------
interpreter.py
-------------------------------------------------------------

Implements the Interpreter for executing the Abstract Syntax Tree (AST).

Purpose:

The interpreter takes the parsed AST and executes the program, evaluating expressions and handling variable assignments.

Responsibilities:

Stores variable values in a symbol table.

Provides methods to visit different types of nodes in the AST.

Handles the following node types:

Program
Assign
Print
Binary operations (e.g., +, -, *, /, <, >, %)
Unary operations (e.g., +, -)
Numeric values
String values
Variable references

Main Entry Point:

`interpret(ast)`: Accepts the root of the AST and initiates the execution by visiting the appropriate nodes.


-------------------------------------------------------------
coderunner.py
-------------------------------------------------------------

Serves as the entry point for executing the pseudo-programming language.

Purpose:

Reads source code from a file, tokenizes it, parses it into an AST, and then interprets the AST.

Workflow:

1. Read the pseudocode from a specified file passed as an argument from the terminal.
2. Initialize the lexer to create tokens from the source code.
3. Create a parser to convert the token stream into an AST.
4. Use the interpreter to execute the AST.

Usage Example:

To run a script named `script.txt`:

python coderunner.py script.txt

This command reads `script.txt`, processes the code, and executes it, printing results to the console.
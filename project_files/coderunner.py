import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

# Read pseudocode file
with open(sys.argv[1], 'r') as f:
    source_code = f.read()

# Parse it
lexer = Lexer(source_code)
parser = Parser(lexer)
ast = parser.program()

# Interpret it
interpreter = Interpreter()
interpreter.interpret(ast)
from dataclasses import dataclass

class TokenType:
    # Single-character tokens
    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"
    ASSIGN = "ASSIGN"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    SEMI = "SEMI"

    # Addition: Math Operands
    LESSTHAN = "LESSTHAN"
    MORETHAN = "MORETHAN"
    MODULUS = "MODULUS"

    # Multi-character tokens
    NUMBER = "NUMBER"
    ID = "ID"
    LET = "LET"
    PRINT = "PRINT"
    STRING = "STRING"

    EOF = "EOF"


@dataclass
class Token:
    type: str
    value: object
    pos: int

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


KEYWORDS = {
    "let": TokenType.LET,
    "print": TokenType.PRINT,
}

from tokens import TokenType
from lexer import Lexer
from ast_nodes import (
    Program, Assign, Print,
    BinOp, UnaryOp, Num, Var
)


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise SyntaxError(
                f"Expected {token_type}, got {self.current_token.type} at pos {self.current_token.pos}"
            )

    def program(self):
        statements = self.statement_list()
        self.eat(TokenType.EOF)
        return Program(statements)

    def statement_list(self):
        statements = [self.statement()]
        self.eat(TokenType.SEMI)

        while self.current_token.type != TokenType.EOF:
            if self.current_token.type in (TokenType.LET, TokenType.PRINT):
                statements.append(self.statement())
                self.eat(TokenType.SEMI)
            elif self.current_token.type == TokenType.SEMI:
                self.eat(TokenType.SEMI)
            else:
                break

        return statements

    def statement(self):
        if self.current_token.type == TokenType.LET:
            return self.assignment()

        elif self.current_token.type == TokenType.PRINT:
            return self.print_stmt()

        else:
            raise SyntaxError(f"Unexpected statement at pos {self.current_token.pos}")

    def assignment(self):
        self.eat(TokenType.LET)
        name = self.current_token
        self.eat(TokenType.ID)
        self.eat(TokenType.ASSIGN)
        expr = self.expr()
        return Assign(name.value, expr)

    def print_stmt(self):
        self.eat(TokenType.PRINT)
        self.eat(TokenType.LPAREN)
        expr = self.expr()
        self.eat(TokenType.RPAREN)
        return Print(expr)

    def expr(self):
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token
            self.eat(op.type)
            node = BinOp(node, op, self.term())

        return node

    def term(self):
        node = self.factor()

        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            op = self.current_token
            self.eat(op.type)
            node = BinOp(node, op, self.factor())

        return node

    def factor(self):
        tok = self.current_token

        if tok.type in (TokenType.PLUS, TokenType.MINUS):
            self.eat(tok.type)
            return UnaryOp(tok, self.factor())

        if tok.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Num(tok.value)

        if tok.type == TokenType.ID:
            self.eat(TokenType.ID)
            return Var(tok.value)

        if tok.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node

        raise SyntaxError(f"Unexpected token {tok} at pos {tok.pos}")

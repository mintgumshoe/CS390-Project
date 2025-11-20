from tokens import Token, TokenType, KEYWORDS


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current = text[0] if text else None

    def advance(self):
        self.pos += 1
        self.current = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current is not None and self.current.isspace():
            self.advance()

    def peek(self):
        nxt = self.pos + 1
        return self.text[nxt] if nxt < len(self.text) else None

    def number(self):
        start = self.pos
        while self.current is not None and self.current.isdigit():
            self.advance()

        if self.current == "." and self.peek() and self.peek().isdigit():
            self.advance()
            while self.current is not None and self.current.isdigit():
                self.advance()

        literal = self.text[start:self.pos]
        value = float(literal) if "." in literal else int(literal)
        return Token(TokenType.NUMBER, value, start)

    # Addition: String reader
    def read_string(self):
        self.advance()  # Move past the opening quote
        start = self.pos

        while self.current is not None and self.current != '"':
            self.advance()

        if self.current is None:
            raise SyntaxError(f"Unterminated string starting at position {start}")

        value = self.text[start:self.pos]
        self.advance()  # Move past the closing quote
        return Token(TokenType.STRING, value, start)

    def identifier_or_keyword(self):
        start = self.pos
        while self.current is not None and (self.current.isalnum() or self.current == "_"):
            self.advance()

        lexeme = self.text[start:self.pos]
        ttype = KEYWORDS.get(lexeme, TokenType.ID)
        return Token(ttype, lexeme, start)

    def get_next_token(self):
        while self.current is not None:
            ch = self.current

            if ch.isspace():
                self.skip_whitespace()
                continue

            if ch.isdigit():
                return self.number()

            if ch.isalpha() or ch == "_":
                return self.identifier_or_keyword()

            if ch == '"':
                return self.read_string()

            if ch == "+":
                self.advance()
                return Token(TokenType.PLUS, "+", self.pos - 1)

            if ch == "-":
                self.advance()
                return Token(TokenType.MINUS, "-", self.pos - 1)

            if ch == "*":
                self.advance()
                return Token(TokenType.MUL, "*", self.pos - 1)

            if ch == "/":
                self.advance()
                return Token(TokenType.DIV, "/", self.pos - 1)

            if ch == "<":
                self.advance()
                return Token(TokenType.LESSTHAN, "<", self.pos - 1)
            
            if ch == ">":
                self.advance()
                return Token(TokenType.MORETHAN, ">", self.pos - 1)
            
            if ch == "%":
                self.advance()
                return Token(TokenType.MODULUS, "%", self.pos - 1)
            
            if ch == "=":
                self.advance()
                return Token(TokenType.ASSIGN, "=", self.pos - 1)

            if ch == "(":
                self.advance()
                return Token(TokenType.LPAREN, "(", self.pos - 1)

            if ch == ")":
                self.advance()
                return Token(TokenType.RPAREN, ")", self.pos - 1)

            if ch == ";":
                self.advance()
                return Token(TokenType.SEMI, ";", self.pos - 1)

            raise SyntaxError(f"Unexpected character '{ch}' at position {self.pos}")

        return Token(TokenType.EOF, None, self.pos)

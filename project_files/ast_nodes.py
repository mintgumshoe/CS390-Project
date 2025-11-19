from dataclasses import dataclass


class AST:
    pass


@dataclass
class Program(AST):
    statements: list


@dataclass
class Assign(AST):
    name: str
    expr: AST


@dataclass
class Print(AST):
    expr: AST


@dataclass
class BinOp(AST):
    left: AST
    op: object
    right: AST


@dataclass
class UnaryOp(AST):
    op: object
    expr: AST


@dataclass
class Num(AST):
    value: float | int


@dataclass
class Var(AST):
    name: str

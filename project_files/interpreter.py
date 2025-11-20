from typing import Any, Dict

class Interpreter:
    def __init__(self):
        # Symbol table to store variable values
        self.variables: Dict[str, Any] = {}
    
    def visit(self, node) -> Any:
        # Call the appropriate visit method for each node type
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)
    
    def generic_visit(self, node):
        # The method_name isnt one of the ones implemented here
        raise Exception(f'No visit_{type(node).__name__} method defined for {node}')
    
    ## Program and Statement visitors ##

    def visit_Program(self, node) -> None:
        # Visit all statements in the program
        for statement in node.statements:
            self.visit(statement)
    
    def visit_Assign(self, node) -> None:
        # Handle variable assignment: let x = expr;

        value = self.visit(node.expr)
        self.variables[node.name] = value
    
    def visit_Print(self, node) -> None:
        # Handle print statement: print(expr);
        value = self.visit(node.expr)
        print(value)
    
    # Expression visitors
    def visit_BinOp(self, node) -> Any:
        # Handle binary operations: +, -, *, /, etc.
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        operator = node.op.value
        
        if operator == '+':
            return left_val + right_val
        elif operator == '-':
            return left_val - right_val
        elif operator == '*':
            return left_val * right_val
        elif operator == '/':
            return left_val / right_val
        elif operator == '%':
            return left_val % right_val
        elif operator == '<':
            return left_val < right_val
        elif operator == '>':
            return left_val > right_val
        else:
            raise Exception(f'Unknown binary operator: {node.op}')
    
    def visit_UnaryOp(self, node) -> Any:
        # Handle unary operations: -, +, !, etc.
        op_val = self.visit(node.op)
        
        if node.op == '-':
            return -op_val
        elif node.op == '+':
            return op_val
        elif node.op == '!':
            return not op_val
        else:
            raise Exception(f'Unknown unary operator: {node.op}')
    
    def visit_Num(self, node) -> float:
        # Return the numeric value
        return node.value
    
    def visit_Str(self, node) -> str:
        return node.value
    
    def visit_Var(self, node) -> Any:
        # Look up variable value
        if node.name not in self.variables:
            raise Exception(f'Undefined variable: {node.name}')
        return self.variables[node.name]

    def interpret(self, ast) -> None:
        # Main entry point to interpret the AST
        self.visit(ast)

  
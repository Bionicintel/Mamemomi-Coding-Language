class Interpreter:
    def __init__(self):
        self.env = {}

    def eval(self, node):
        if isinstance(node, FunctionDecl):
            self.env[node.name] = node
        elif isinstance(node, Conditional):
            condition = self.eval(node.condition)
            if condition:
                for stmt in node.body:
                    self.eval(stmt)
            else:
                for stmt in node.else_body:
                    self.eval(stmt)
        elif isinstance(node, ReturnStmt):
            return self.eval(node.expression)
        elif isinstance(node, BinaryExpr):
            left = self.eval(node.left)
            right = self.eval(node.right)
            return self.apply_operator(node.operator, left, right)
        elif isinstance(node, Identifier):
            return self.env[node.name]
        elif isinstance(node, Number):
            return int(node.value)
        else:
            raise RuntimeError(f"Unknown AST node type: {type(node)}")

    def apply_operator(self, operator, left, right):
        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        elif operator == "*":
            return left * right
        elif operator == "/":
            return left / right
        else:
            raise RuntimeError(f"Unknown operator: {operator}")
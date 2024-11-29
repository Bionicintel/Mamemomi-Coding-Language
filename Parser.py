class FunctionDecl:
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

class Conditional:
    def __init__(self, condition, body, else_body):
        self.condition = condition
        self.body = body
        self.else_body = else_body

class ReturnStmt:
    def __init__(self, expression):
        self.expression = expression

class Identifier:
    def __init__(self, name):
        self.name = name

class Number:
    def __init__(self, value):
        self.value = value

class BinaryExpr:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self):
        self.pos += 1
        return self.tokens[self.pos - 1] if self.pos <= len(self.tokens) else None

    def parse(self):
        statements = []
        while self.peek():
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
        return statements

    def parse_statement(self):
        if self.peek() and self.peek()[1] == "me":
            return self.parse_function_declaration()
        elif self.peek() and self.peek()[1] == "mi":
            return self.parse_conditional()
        elif self.peek() and self.peek()[1] == "mo":
            return self.parse_return_statement()
        return None

    def parse_function_declaration(self):
        self.consume()  # consume 'me'
        name = self.consume()[1]  # get the function name
        self.consume()  # consume '('
        parameters = self.parse_parameters()
        self.consume()  # consume ')'
        self.consume()  # consume '{'
        body = self.parse_statements()
        self.consume()  # consume '}'
        return FunctionDecl(name, parameters, body)

    def parse_parameters(self):
        parameters = []
        if self.peek() and self.peek()[0] == "IDENTIFIER":
            parameters.append(self.consume()[1])
            while self.peek() and self.peek()[1] == ",":
                self.consume()  # consume ','
                parameters.append(self.consume()[1])
        return parameters

    def parse_statements(self):
        statements = []
        while self.peek() and self.peek()[1] not in ["mi", "ma", "mo", "}"]:
            statements.append(self.parse_statement())
        return statements

    def parse_conditional(self):
        self.consume()  # consume 'mi'
        condition = self.parse_expression()
        self.consume()  # consume '{'
        body = self.parse_statements()
        self.consume()  # consume '}'
        self.consume()  # consume 'ma'
        self.consume()  # consume '{'
        else_body = self.parse_statements()
        self.consume()  # consume '}'
        return Conditional(condition, body, else_body)

    def parse_return_statement(self):
        self.consume()  # consume 'mo'
        expression = self.parse_expression()
        self.consume()  # consume ';'
        return ReturnStmt(expression)

    def parse_expression(self):
        left = self.parse_primary_expression()
        while self.peek() and self.peek()[0] == "OPERATOR":
            operator = self.consume()[1]
            right = self.parse_primary_expression()
            left = BinaryExpr(left, operator, right)
        return left

    def parse_primary_expression(self):
        if self.peek() and self.peek()[0] == "IDENTIFIER":
            return Identifier(self.consume()[1])
        elif self.peek() and self.peek()[0] == "NUMBER":
            return Number(self.consume()[1])
        else:
            raise SyntaxError(f"Unexpected token: {self.peek()}")
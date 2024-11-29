import re

KEYWORDS = ['me', 'mi', 'ma', 'mo']
TOKENS = [
    ('NUMBER', r'\d+'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('OPERATOR', r'[+\-*/]'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('COMMA', r','),
    ('SEMICOLON', r';'),
    ('WHITESPACE', r'\s+'),
]

def lexer(code):
    tokens = []
    position = 0
    while position < len(code):
        matched = False
        for token_type, regex in TOKENS:
            pattern = re.compile(regex)
            match = pattern.match(code, position)
            if match:
                if token_type != 'WHITESPACE':  # Skip whitespaces
                    tokens.append((token_type, match.group(0)))
                position = match.end()
                matched = True
                break
        if not matched:
            raise SyntaxError(f"Unexpected character at position {position}")
    return tokens
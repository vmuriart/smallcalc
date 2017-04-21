from smallcalc import calc_lexer as clex


class Node:

    def asdict(self):
        return {}  # pragma: no cover


class ValueNode(Node):

    node_type = 'value_node'

    def __init__(self, value):
        self.value = value

    def asdict(self):
        return {
            'type': self.node_type,
            'value': self.value
        }


class IntegerNode(ValueNode):
    node_type = 'integer'

    def __init__(self, value):
        self.value = int(value)


class LiteralNode(ValueNode):

    node_type = 'literal'


class BinaryNode(Node):

    node_type = 'binary'

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def asdict(self):
        result = {
            'type': self.node_type,
            'left': self.left.asdict()
        }

        result['right'] = None
        if self.right:
            result['right'] = self.right.asdict()

        result['operator'] = None
        if self.operator:
            result['operator'] = self.operator.asdict()

        return result


class CalcParser:

    def __init__(self):
        self.lexer = clex.CalcLexer()

    def parse_addsymbol(self):
        t = self.lexer.get_token()
        return LiteralNode(t.value)

    def parse_integer(self):
        t = self.lexer.get_token()
        return IntegerNode(t.value)

    def parse_factor(self):
        next_token = self.lexer.peek_token()

        if next_token.type == clex.LITERAL and next_token.value == '(':
            self.lexer.get_token()
            expression = self.parse_expression()
            self.lexer.get_token()
            return expression

        return self.parse_integer()

    def parse_term(self):
        left = self.parse_factor()

        next_token = self.lexer.peek_token()

        if next_token.type == clex.LITERAL and next_token.value in ['*', '/']:
            operator = self.parse_addsymbol()
            right = self.parse_term()

            return BinaryNode(left, operator, right)

        return left

    def parse_expression(self):
        left = self.parse_term()

        next_token = self.lexer.peek_token()

        if next_token.type == clex.LITERAL and next_token.value in ['+', '-']:
            operator = self.parse_addsymbol()
            right = self.parse_expression()

            return BinaryNode(left, operator, right)

        return left

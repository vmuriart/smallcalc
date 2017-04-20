from smallcalc import calc_visitor as cvis


def test_visitor_integer():
    ast = {
        'type': 'integer',
        'value': 12
    }

    v = cvis.CalcVisitor()
    assert v.visit(ast) == (12, 'integer')


def test_visitor_expression_sum():
    ast = {
        'type': 'binary',
        'left': {
                'type': 'integer',
                'value': 5
        },
        'right': {
            'type': 'integer',
            'value': 4
        },
        'operator': {
            'type': 'literal',
            'value': '+'
        }
    }

    v = cvis.CalcVisitor()
    assert v.visit(ast) == (9, 'integer')


def test_visitor_expression_subtraction():
    ast = {
        'type': 'binary',
        'left': {
                'type': 'integer',
                'value': 5
        },
        'right': {
            'type': 'integer',
            'value': 4
        },
        'operator': {
            'type': 'literal',
            'value': '-'
        }
    }

    v = cvis.CalcVisitor()
    assert v.visit(ast) == (1, 'integer')


def test_visitor_expression_with_multiple_operations():
    ast = {
        'type': 'binary',
        'left': {
            'type': 'integer',
            'value': 200
        },
        'right': {
            'type': 'binary',
            'left': {
                'type': 'integer',
                'value': 3
            },
            'right': {
                'type': 'integer',
                'value': 4
            },
            'operator': {
                'type': 'literal',
                'value': '-'
            }
        },
        'operator': {
            'type': 'literal',
            'value': '+'
        }
    }

    v = cvis.CalcVisitor()
    assert v.visit(ast) == (199, 'integer')

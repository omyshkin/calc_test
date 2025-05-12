def evaluate_expression(expr):
    try:
        result = eval(expr)
        return result
    except Exception as e:
        return str(e)
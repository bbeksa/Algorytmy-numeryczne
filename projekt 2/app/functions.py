from sympy import var, diff, sympify


def function_value(fun, val):
    x = var('x')
    # definiuje x w wyrażeniu jako zmienną
    expr = sympify(fun)
    # zamienia stringa na obliczlne wyrażenie
    return expr.subs(x, val)
    # oblicza wartość expr kiedy za x podstawimy val


def derivative_value(fun, val):
    x = var('x')
    expr = diff(sympify(fun))
    return expr.subs(x, val)


def count(fun, x, n):
    if n == 1:
        return x - (function_value(fun, x)) / derivative_value(fun, x)
    else:
        return count(fun, x, n - 1) - (function_value(fun, count(fun, x, n - 1))) / derivative_value(fun,
                                                                                                     count(fun, x,
                                                                                                           n - 1))

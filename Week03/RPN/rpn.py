from math import sqrt

def get_float_list(lst):
    return [float(i) for i in lst]

def pop_last_two(lst):
    lst.pop()
    lst.pop()
    return lst

def rpn_calculate(expression):
    split_expr = expression.split(' ')
    if len(split_expr) == 1:
        return float(split_expr[0])
    operands_stack = []
    operators_list = ['+', '-', '*', '/']
    expr_idx = 0
    while len(operands_stack) >= 0 and expr_idx < len(split_expr):
        current_expr = split_expr[expr_idx]
        if len(operands_stack) > 1 and current_expr in operators_list:
            to_calculate = operands_stack[len(operands_stack) - 2] + current_expr + operands_stack[len(operands_stack) - 1]
            result = eval(to_calculate)
            pop_last_two(operands_stack)
            operands_stack.append(str(result))
        elif len(operands_stack) == 1 and current_expr == '-':
            result = -float(operands_stack.pop())
            operands_stack.append(str(result))
        elif current_expr == 'SQRT':
            result = sqrt(float(operands_stack.pop()))
            operands_stack.append(str(result))
        elif current_expr == 'MAX':
            result = max(get_float_list(operands_stack))
            operands_stack.clear()
            operands_stack.append(str(result))
        elif current_expr == 'MIN':
            result = min(get_float_list(operands_stack))
            operands_stack.clear()
            operands_stack.append(str(result))
        else:
            operands_stack.append(current_expr)
        expr_idx += 1
    return float(operands_stack[0])

def main():
    print(rpn_calculate('4 2 + 3 -'))
    print(rpn_calculate('3 5 8 * 7 + *'))
    print(rpn_calculate('20 3 /'))
    print(rpn_calculate('9 SQRT'))
    print(rpn_calculate('4 -'))

if __name__ == '__main__':
    main()

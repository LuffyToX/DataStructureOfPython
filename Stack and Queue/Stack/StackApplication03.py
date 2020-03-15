# -*- coding: utf-8 -*-
# 中缀表达式转换为后缀表达式并求值


from SequenceStack import SStack


class ESStack(SStack):
    def __init__(self):
        super().__init__()

    def depth(self):
        """
        检查栈深度  ==>
                          如果处理运算符时栈中元素不足两个，操作就应该失败
                          处理完整个表达式时，栈里应该只剩下计算结果
        """

        return len(self._elems)


def splitExpressionToList(line):
    """ 将表达式切分成项列表（仅支持每个项以空格分隔的情形）"""
    return line.split()


def suffixExpressionCalculation(exp):
    """ 计算后缀表达式 """

    suffixOperators = "+-*/"                    # 运算符
    ss = ESStack()

    items = splitExpressionToList(exp)    # items 是一个项的表
    for x in items:
        if x not in suffixOperators:      # 遇到运算对象，压栈
            ss.push(float(x))
            continue

        if ss.depth() < 2:                # 此处 x 必为运算符，栈元素（只考虑二元运算）不够时抛出异常
            raise SyntaxError
        b = ss.pop_()                     # 取得第二个运算对象
        a = ss.pop_()                     # 取得第一个运算对象

        if x == "+":
            c = a + b
        elif x == "-":
            c = a - b
        elif x == "*":
            c = a * b
        else:
            c = a / b

        ss.push(c)                        # 将运算结果压栈

    if ss.depth() == 1:
        return ss.pop_()
    raise SyntaxError


def transformInfixToSufix(exp):
    """ 将中缀表达式转换为后缀表达式 """

    # 为每个运算符关联一个优先级
    # 这里给 '(' 关联了一个很低的优先级，保证其他运算符都不会将其弹出，只有对应的 ')' 才能弹出它
    priority = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5}
    infixOperators = "+-*/()"
    ss = ESStack()
    output = list()                                           # 存储后缀表达式项

    items = splitExpressionToList(exp)
    for x in items:
        if x not in infixOperators:                           # 运算对象直接送出
            output.append(x)
        elif ss.is_empty() or x == '(':                       # 左括号进栈
            ss.push(x)
        elif x == ')':                                        # 处理右括号
            while not ss.is_empty() and ss.top() != '(':
                output.append(ss.pop_())
            if ss.is_empty():                                 # 没找到左括号，就是不匹配
                raise SyntaxError("括号不配对")
            ss.pop_()                                         # 弹出左括号，右括号也不压栈
        else:
            while not ss.is_empty() and priority[ss.top()] >= priority[x]:
                output.append(ss.pop_())
            ss.push(x)                                        # 算术运算符压栈

    while not ss.is_empty():                                  # 送出栈里剩下的运算符
        if ss.top() == '(':                                   # 如果还有左括号，就是不配对
            raise SyntaxError("括号不配对")
        output.append(ss.pop_())

    return output


if __name__ == "__main__":
    #expression = "5 3 + 6 * 2 /"
    expression = "( 5 + 3 ) * 6 / 2"
    print(transformInfixToSufix(expression))

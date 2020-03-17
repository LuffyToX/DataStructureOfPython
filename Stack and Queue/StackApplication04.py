# -*- coding: utf-8 -*-
# 中缀表达式求值


from SequenceStack import SStack


class ESStack(SStack):
    def __init__(self):
        super().__init__()

    def depth(self):
        return len(self._elems)


class Infix:
    def __init__(self, exp):
        self.exp = exp


    def compare(self, op1, op2):
        """ 比较两个运算符的优先级 """
        return op1 in ["*", "/"] and op2 in ["+", "-"]


    def getvalue(self, num1, num2, operator):
        """ 根据运算符 operator 计算结果并返回 """

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        else:
            return num1 / num2


    def process(self, data, opt):
        """ opt 出栈一个运算符，data 出栈两个运算对象，进行一次计算，并将结果压入 data 栈 """

        operator = opt.pop_()
        num2 = data.pop_()
        num1 = data.pop_()
        data.push(self.getvalue(num1, num2, operator))


    def calculate(self):
        """ 计算字符串表达式的值，字符串中不包含空格 """

        data = ESStack()                     # 运算对象栈
        opt = ESStack()                      # 运算符栈
        i = 0                                # 表达式遍历索引
        while i < len(self.exp):
            # 将运算对象压入 data 栈
            if self.exp[i].isdigit():
                start = i
                while i+1 < len(self.exp) and self.exp[i+1].isdigit():
                    i += 1
                data.push(float(self.exp[start: i+1]))

            # 遇到右括号 opt 出栈，同时 data 也出栈并计算，计算结果压入 data 栈，直到 opt 出栈一个左括号
            elif self.exp[i] == ")":
                while opt.top() != "(":
                    self.process(data, opt)
                # 出栈 '('
                opt.pop_()

            # 运算符栈为空或者运损符栈顶为左括号，将该运算符直接压入 opt 栈
            elif opt.depth() == 0 or opt.top() == "(":
                opt.push(self.exp[i])

            # 当前操作符为左括号或者比栈顶操作符优先级高，将该运算符直接压入 opt 栈
            elif self.exp[i] == "(" or self.compare(self.exp[i], opt.top()):
                opt.push(self.exp[i])

            # 优先级不比栈顶运算符高时 opt 出栈，同时 data 出栈并计算，计算结果压入 data 栈
            else:
                while opt.depth() != 0 and not self.compare(self.exp[i], opt.top()):
                    # 若遇到左括号，停止计算
                    if opt.top() == "(":
                        break
                    self.process(data, opt)
                opt.push(self.exp[i])
            i += 1
        while opt.depth() != 0:
            self.process(data, opt)

        return data.pop_()


if __name__ == '__main__':
    expression = "(9+((3-1)*3+10/2))*2"
    infix = Infix(expression)
    print(infix.calculate())

# -*- coding: utf-8 -*-
# 顺序栈


class SStack:
    def __init__(self):
        """ 构造空栈 """

        self._elems = list()

    def is_empty(self):
        """ 判空 """

        return not self._elems

    def top(self):
        """ 取栈顶元素 """

        if self.is_empty():
            raise ValueError
        return self._elems[-1]

    def push(self, elem):
        """ 压栈 """

        self._elems.append(elem)

    def pop_(self):
        """ 出栈 """

        if self.is_empty():
            raise ValueError
        return self._elems.pop()
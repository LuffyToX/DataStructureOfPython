# -*- coding: utf-8 -*-
# 链栈


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack:
    def __init__(self):
        """ 创建空栈 """

        self._top = None

    def is_empty(self):
        """ 判空 """

        return not self._top

    def top(self):
        """ 取栈顶元素 """

        if self.is_empty():
            raise ValueError
        return self._top.elem

    def push(self, elem):
        """ 压栈 """

        self._top = LNode(elem, self._top)

    def pop_(self):
        """ 出栈 """

        if self.is_empty():
            raise ValueError
        val = self._top
        self._top = val.next
        return val.elem


if __name__ == "__main__":
    ls = LStack()
    ls.push(6)
    ls.push(5)
    ls.push(4)
    ls.push(3)
    ls.push(2)
    ls.push(1)

    while not ls.is_empty():
        print(ls.pop_(), end=' ')

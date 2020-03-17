# -*- coding: utf-8 -*-
# 顺序栈
# 用 list 对象 _elems 存储栈中元素
# 所有栈操作都映射到 list 操作
# 顺序栈把表尾当作栈顶 O(1)


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


if __name__ == "__main__":
    ss = SStack()
    ss.push(6)
    ss.push(5)
    ss.push(4)
    ss.push(3)
    ss.push(2)
    ss.push(1)

    while not ss.is_empty():
        print(ss.pop_(), end=' ')



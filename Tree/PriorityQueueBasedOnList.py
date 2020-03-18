# -*- coding: utf-8 -*-
# 优先队列：list + 在存入元素时保证表中元素始终按优先顺序排列


class PrioQue:
    def __init__(self, lst=[]):
        self._elems = list(lst)              # lst 可以是任何迭代序列
        self._elems.sort(reverse=True)       # 以较小作为比较优先


    def is_empty(self):
        """ 判空 """

        return not self._elems


    def enqueue(self, elem):
        """ 入队 O(n) """

        i = len(self._elems)-1
        while i >= 0:                        # 从后往前检查
            if self._elems[i] <= elem:
                i -= 1
            else:
                break
        self._elems.insert(i+1, elem)        # 找到位置后插入


    def dequeue(self):
        """ 出队 """

        if self.is_empty():
            raise ValueError
        return self._elems.pop()


    def peek(self):
        """ 检查最优先元素 """

        if self.is_empty():
            raise ValueError
        return self._elems[-1]


if __name__ == "__main__":
    priq = PrioQue([1, 4, 2, 5])
    priq.enqueue(10)
    print(priq.dequeue())

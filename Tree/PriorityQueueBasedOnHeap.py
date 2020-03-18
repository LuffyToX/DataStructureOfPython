# -*- coding: utf-8 -*-
# 优先队列：堆


class PrioQueue:
    def __init__(self, lst=[]):
        self._elems = list(lst)               # lst 可以是任何迭代序列
        if lst:
            self.buildheap()                  # 将 list 转换成堆


    def is_empty(self):
        """ 判空 """

        return not self._elems


    def peek(self):
        """ 取堆顶元素 """

        if self.is_empty():
            raise ValueError
        return self._elems[0]


    def enqueue(self, elem):
        """ 入队  O(logn)"""

        self._elems.append(None)                       # 在表尾添加一个空结点
        self.situp(elem, len(self._elems)-1)


    def situp(self, elem, last):
        """ 入队调整堆序 """

        elems, i, j = self._elems, last, (last-1)//2   # i 当前结点；j 当前结点的父结点
        while i > 0 and elem < elems[j]:
            elems[i] = elems[j]                        # 将此时父结点中的元素移到当前结点位置
            i, j = j, (j-1)//2
        elems[i] = elem                                # 直到找到合适位置，将元素填入


    def dequeue(self):
        """ 出队 """

        if self.is_empty():
            raise ValueError
        elems = self._elems
        val = elems[0]                                 # 堆顶（最优元素）
        e = elems.pop()
        if len(elems) > 0:
            self.sitdown(e, 0, len(elems))
        return val


    def sitdown(self, elem, begin, end):
        """ 出队调整堆序 """

        elems, i, j = self._elems, begin, begin*2+1    # i 当前结点；j 当前结点的左子结点
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:    # j+1 当前结点的右子结点
                j += 1
            if elem < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = elem


    def buildheap(self):
        """ 构建堆 """

        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.sitdown(self._elems[i], i, end)


if __name__ == "_main__":
    pass
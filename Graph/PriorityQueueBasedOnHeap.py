# -*- coding: utf-8 -*-
# 基于堆的优先队列


class PrioQueue:
    def __init__(self, lst=[]):
        self._elems = list(lst)                        # lst 可以是任何迭代序列
        if lst:
            self.buildheap()                           # 将 list 转换成堆


    def is_empty(self):
        """ 判空 """

        return not self._elems


    def peek(self):
        """ 取堆顶元素 """

        if self.is_empty():
            raise ValueError
        return self._elems[0]                          # 以表首作为堆顶


    def enqueue(self, elem):
        """ 入队 """

        self._elems.append(None)                       # 在表尾添加元素（堆末尾）
        self.siftup(elem, len(self._elems)-1)          # 向上筛选


    def siftup(self, elem, last):
        """ 入队调整堆序（向上筛选）O(logn) """

        elems, i, j = self._elems, last, (last-1)//2   # i 当前结点；j 当前结点的父结点
        while i > 0 and elem < elems[j]:
            elems[i] = elems[j]                        # 将此时父结点中的元素移到当前结点位置
            i, j = j, (j-1)//2                         # 沿堆序向上查找
        elems[i] = elem                                # 直到找到合适位置，将元素填入


    def dequeue(self):
        """ 出队 """

        if self.is_empty():
            raise ValueError
        elems = self._elems
        val = elems[0]                                 # 堆顶（表首，最优元素）
        e = elems.pop()                                # 弹出表尾元素（堆尾元素）
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))            # 将弹出的表尾（堆尾）元素插入合适的位置
        return val


    def siftdown(self, elem, begin, end):
        """ 出队调整堆序（向下筛选）O(logn)"""

        elems, i, j = self._elems, begin, begin*2+1    # i 当前结点；j 当前结点的左子结点
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:    # j+1 当前结点的右子结点
                j += 1                                 # 找当前结点的最小子结点
            if elem < elems[j]:                        # 如果堆尾元素小于该子结点，则找到插入位置
                break
            elems[i] = elems[j]                        # 将此时最小子结点中的元素移到当前结点位置
            i, j = j, 2*j+1                            # 沿堆序向下查找
        elems[i] = elem                                # 直到找到合适位置，将元素填入


    def buildheap(self):
        """ （初始）构建堆 O(n) """

        # 把初始表看作一棵完全二叉树，则 [len(lst)//2, len(lst)) 都是叶结点，即它们中的每一个已是一个堆
        # 从完全二叉树的最下最右分支结点 end//2-1 开始向左一个个建堆，继而上一层，直至整个表建成一个堆
        # 从第一个叶结点 end//2 开始也可，只是第一次循环不会发生任何改变
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)
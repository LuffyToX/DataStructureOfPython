# -*- coding: utf-8 -*-
# 顺序队列


class SQueue:
    def __init__(self, initLen=4):
        self._len = initLen                  # 存储区的长度
        self._elems = [0]*initLen            # 元素存储列表
        self._head = 0                       # 队头元素下标
        self._num = 0                        # 元素实际个数


    def is_empty(self):
        """ 判空 """

        return self._num == 0


    def peek(self):
        """ 查看队头元素（不删除） """

        if self.is_empty():
            raise ValueError
        return self._elems[self._head]


    def enqueue(self, elem):
        """ 入队 """

        # 队满，扩充存储区
        if self._num == self._len:
            self.extend_()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1

    def dequeue(self):
        """ 出队 """

        # 队空
        if self.is_empty():
            raise ValueError
        val = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return val


    def extend_(self):
        """ 扩充存储区 """

        oldLen = self._len
        self._len *= 2                                              # 每次扩充两倍
        newElems = [0]*self._len                                    # 新的存储区列表
        for i in range(oldLen):                                     # 将元素复制到新存储区
            newElems[i] = self._elems[(self._head + i) % oldLen]
        self._elems, self._head = newElems, 0
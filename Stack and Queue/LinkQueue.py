# -*- coding: utf-8 -*-
# 链接队列


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LQueue:
    def __init__(self):
        """ 构造空队列 """

        self._head = None
        self._rear = None


    def is_empty(self):
        """ 判空  """

        return not self._head


    def enqueue(self, elem):
        """ 入队 """

        if self.is_empty():
            # 空队列
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next


    def dequeue(self):
        """ 出队 """

        # 空队列  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        val = self._head.elem               # 保存队头元素
        self._head = self._head.next        # 将头指针指向第二个结点
        if self._head is None:
            # 只有一个结点，尾指针要指向 None
            self._rear = None
        return val


    def value(self):
        """ 返回队头元素 """

        if self.is_empty():
            raise ValueError
        return self._head.elem


if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    lq.enqueue(5)
    lq.enqueue(6)

    while not lq.is_empty():
        print(lq.dequeue(), end=' ')



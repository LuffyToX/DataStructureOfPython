# -*- coding: utf-8 -*-
# <双链表>
# 两端的插入和删除操作都能在 O(1) 时间内完成
# 每个结点都需要增加一个链接域，增加的空间开销与结点数成正比，O(n)
# 从双链表中任一结点出发，可以直接找到其前后的相邻结点， O(1)


class DLNode:
    """ 双链表结点类 """
    def __init__(self, elem, prev_=None, next_=None):
        # 双链表的结点类是一个三元组：(elem, prev, next)
        # elem：保存作为表元素的数据项
        # prev：保存上一个结点的标识
        # next：保存下一个结点的标识
        self.elem = elem
        self.prev = prev_
        self.next = next_


class DLList:
    def __init__(self):
        """ 构造空表 """

        # 表头指针  ==>  保存着这个表的首结点的引用
        # 表尾指针  ==>  保存着这个表的尾结点的引用
        # 创建空表  ==>  将表头和表尾指针设置为空链接  ==>  O(1)
        self._head = None
        self._rear = None

    def is_empty(self):
        """
        判空  ==>  O(1) """

        # 表头/表尾 指针的值是空链接 (None)  ==>  空表
        return self._head is None

    def prepend(self, elem):
        """
        头插  ==>  O(1) """

        # 创建新结点，并将其后继指向头指针
        p = DLNode(elem, None, self._head)
        if self.is_empty():
            # 空表  ==>  表尾指针指向新结点
            self._rear = p
        else:
            # 非空  ==>  不需要修改表尾指针
            p.next.prev = p
        # 表头指针指向新结点
        self._head = p

    def append_(self, elem):
        """
        尾插  ==>  O(1) """

        # 创建新结点，并将其前驱指向尾指针
        p = DLNode(elem, self._rear, None)
        if self.is_empty():
            # 空表  ==>  头指针指向新结点
            self._head = p
        else:
            # 非空  ==>  不需要修改头指针
            p.prev.next = p
        # 表尾指针指向新结点
        self._rear = p

    def insert_(self, elem, i):
        """
        一般位置的插入  ==>  O(n) """

        # 下标合法性检查
        if i < 0 or i > len(self):
            raise IndexError

        # 头插（头/尾插处理了空表的情形）
        if i == 0 or self.is_empty():
            self.prepend(elem)
            return

        # 尾插
        if i == len(self):
            self.append_(elem)
            return

        # 以下代码不能处理只有一个结点的情形
        # 但是如果只有一个结点代码运行不到此处
        # 头插/尾插均可以处理只有一个结点的情形
        pre = self._head
        while i > 1:          # 循环结束  ==>  pre 指向目标结点的前一结点
            i -= 1
            pre = pre.next
        # 创建新结点，并将其前驱指向 pre、后继指向 pre.next
        q = DLNode(elem, pre, pre.next)
        pre.next.prev = q
        pre.next = q

    def del_first(self):
        """
        删除表头结点，并返回其元素  ==>  O(1) """

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        val = self._head.elem          # 保存表首元素
        self._head = self._head.next   # 将头指针指向第二个结点
        if self._head is None:
            # 只有一个结点，尾指针要指向 None
            self._rear = None
        else:
            # 不止一个结点，将原第二个结点的前驱指向 None
            self._head.prev = None
        return val

    def del_last(self):
        """
        删除表尾结点，并返回其元素  ==>  O(1) """

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        val = self._rear.elem           # 保存表尾元素
        self._rear = self._rear.prev    # 将尾指针指向倒数第二个结点
        if self._rear is None:
            # 只有一个元素，头指针要指向 None
            self._head = None
        else:
            # 不止一个结点，将原倒数第二个结点的后继指向 None
            self._rear.next = None
        return val

    def del_all(self):
        """
        删除链表 ==> O(1) ==> 将表头指针指向 None """

        self._head = None

    def delete_(self, i):
        """
        一般位置的删除  ==>  O(n) """

        # 下标合法性检查（注意，这里要 -1）
        if i < 0 or i > len(self)-1:
            raise IndexError

        # 头删（头/尾删处理了空表的情形）
        if i == 0 or self.is_empty():
            self.del_first()
            return

        # 尾删
        if i == len(self)-1:
            self.del_last()
            return

        pre = self._head
        while i > 1:                # 循环结束  ==>  pre 指向目标结点的前一结点
            i -= 1
            pre = pre.next
        pre.next = pre.next.next    # 修改目标结点前驱结点的 next 域
        pre.next.prev = pre         # 修改目标结点后继结点的 prev 域

    def search_i(self, i):
        """
        按下标定位  ==>  确定第 i 个元素所在结点  ==>  O(n) 尾结点可以达到 O(1) """

        # 下标合法性检查（注意这里要 -1）
        if i < 0 or i > len(self)-1:
            raise IndexError

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        if i == len(self)-1:
            return self._rear
        else:
            p = self._head
            while i > 0:           # 循环结束  ==>  p 是目标结点
                i -= 1
                p = p.next
            return p

    def search_elem(self, elem):
        """
        按元素定位  ==>  确定元素 elem 所在结点的下标  ==>  O(n) """

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        p, i = self._head, 0

        # 循环结束可能出现两种情况：
        #                         1. 扫描完表中所有结点还没有找到元素为 elem 的结点
        #                         2. i 的值就是 elem 结点的下标
        while p is not None and p.elem != elem:
            p = p.next
            i = i + 1
        if p is not None:
            return i
        else:
            raise ValueError

    def __len__(self):
        """
        表长  ==>  O(n) """

        p, n = self._head, 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def travel(self):
        """
        遍历  ==>  打印所有结点包含的元素值 """

        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:  # p 不是尾结点
                print(' <--> ', end='')
            p = p.next
        print('')

    def elements(self):
        """
        生成器  ==>  for x in llist.elements() """

        p = self._head
        while p is not None:
            yield p.elem
            p = p.next


if __name__ == "__main__":
    dllist = DLList()
    dllist.prepend(6)
    dllist.prepend(5)
    dllist.prepend(4)
    dllist.prepend(3)
    dllist.prepend(2)
    dllist.prepend(1)
    dllist.travel()

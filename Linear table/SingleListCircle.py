# -*- coding: utf-8 -*-
# <循环单链表>
# 最后一个结点的 next 域不是 None，而是指向表的第一个结点
# 表头指针  ==>  表头插入 O(1)、表头删除 O(1)、表尾插入 O(n)、表尾删除 O(n)
# 表尾指针  ==>  表头插入 O(1)、表头删除 O(1)、表尾插入 O(1)、表尾删除 O(n)  ==>  更好


class LNode:
    """ 结点类 """
    def __init__(self, elem, next_=None):
        # elem：保存作为表元素的数据项
        # next：保存下一个结点的标识
        self.elem = elem
        self.next = next_


class LListCircle:
    def __init__(self):
        """ 构造空表 """

        # 表尾指针  =>  保存着这个表的首结点的引用
        # 创建空表  =>  将表尾指针设置为空链接  =>  O(1)
        self._rear = None

    def is_empty(self):
        """
        判空  ==>  O(1)  ==>  链表一般不会满，除非程序用完了可用的存储空间 """

        # 表尾指针的值是空链接 (None)  =>  空表
        return self._rear is None

    def prepend(self, elem):
        """
        头插  ==>  O(1)  ==>  在尾结点和首结点之间加入新的首结点，尾指针不变 """

        q = LNode(elem)
        if self.is_empty():
            # 空表  =>  建立一个循环
            q.next = q
            self._rear = q
        else:
            # 非空表
            q.next = self._rear.next
            self._rear.next = q

    def append_(self, elem):
        """
        尾插  ==>  O(1)  ==>  在尾结点和首结点之间加入新的尾结点，修改尾指针 """

        # 只是比头插多了一步  =>  修改尾指针
        self.prepend(elem)
        self._rear = self._rear.next

    def insert_(self, elem, i):
        """
        一般位置的插入  ==>  O(n) """

        # 下标合法性检查
        if i < 0 or i > len(self):
            raise IndexError

        # 空表  =>  建立一个循环
        if self.is_empty():
            q = LNode(elem)
            q.next = q
            self._rear = q
            return

        # 头插
        if i == 0:
            self.prepend(elem)
            return

        # 尾插
        if i == len(self):
            self.append_(elem)
            return

        pre = self._rear.next
        while i > 1:              # 循环结束  ==>  pre 指向目标结点的前一结点
            i -= 1
            pre = pre.next
        pre.next = LNode(elem, pre.next)

    def del_first(self):
        """
        删除表头结点，并返回其元素  ==>  O(1) """

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        p = self._rear.next
        if self._rear is p:
            # 只有一个结点
            self._rear = None
        else:
            # 不止一个结点
            self._rear.next = p.next
        return p.elem

    def del_last(self):
        """
        删除表尾结点，并返回表尾元素  ==>  O(n) """

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        pre = self._rear.next
        while pre.next is not self._rear:   # 循环结束  =>  pre 指向尾结点的前一结点
            pre = pre.next
        val = pre.next.elem                 # 保存表尾元素
        pre.next = self._rear.next          # 新的尾结点指向首结点
        self._rear = pre                    # 尾指针指向新的尾结点
        return val

    def del_all(self):
        """
        删除链表 ==> O(1) ==> 将表尾指针赋值为 None (解释器的存储管理系统会自动回收不用的内存) """

        self._rear = None

    def delete_(self, i):
        """
        一般位置的删除  ==>  O(n) """

        # 下标合法性检查（注意，这里要 -1）
        if i < 0 or i > len(self)-1:
            raise IndexError

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        # 头删
        if i == 0:
            self.del_first()
            return

        # 尾删
        if i == len(self)-1:
            self.del_last()
            return

        pre = self._rear.next
        while i > 1:            # 循环结束  ==>  pre 指向目标结点的前一结点
            i -= 1
            pre = pre.next
        pre.next = pre.next.next

    def search_i(self, i):
        """
        按下标定位  ==>  确定第 i 个元素所在结点  ==>  O(n) """

        # 下标合法性检查（注意这里要 -1）
        if i < 0 or i > len(self)-1:
            raise IndexError

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        p = self._rear.next
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

        p, i = self._rear.next, 0

        # 循环结束可能出现两种情况：
        #                         1. 扫描完表中所有结点还没有找到元素为 elem 的结点
        #                         2. i 的值就是 elem 结点的下标
        while p.elem != elem:
            p = p.next
            i = i + 1
            if i > len(self)-1:
                break
        if i < len(self):
            return i
        else:
            raise ValueError

    def __len__(self):
        """
        表长  ==>  O(n) """

        # 空表
        if self.is_empty():
            return 0

        p, n = self._rear.next, 0
        while True:
            n = n + 1
            if p is self._rear:
                break
            p = p.next
        return n

    def travel(self):
        """
        遍历  ==>  打印所有结点包含的元素值 """

        # 空表
        if self.is_empty():
            return

        p = self._rear.next
        while True:
            print(p.elem, end='')
            if p is self._rear:
                break
            else:
                print(' --> ', end='')
            p = p.next
        print('')

    def elements(self):
        """
        生成器  ==>  for x in llist.elements() """

        # 空表
        if self.is_empty():
            return

        p = self._rear.next
        while True:
            yield p.elem
            if p is self._rear:
                break
            p = p.next


if __name__ == "__main__":
    llist = LListCircle()
    llist.prepend(6)
    llist.prepend(5)
    llist.prepend(4)
    llist.prepend(3)
    llist.prepend(2)
    llist.prepend(1)
    llist.travel()

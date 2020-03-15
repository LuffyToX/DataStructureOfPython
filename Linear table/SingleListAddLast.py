# -*- coding: utf-8 -*-
# <添加尾指针的单链表>
# 单链表有一个缺点：尾端加入元素操作的效率低（只能从表头开始查找）
# 对表对象增加一个表尾结点引用域，有了这个引用域，只需常量时间就能找到尾结点


class LNode:
    def __init__(self, elem, next_=None):
        # elem：保存作为表元素的数据项
        # next：保存下一个结点的标识
        self.elem = elem
        self.next = next_


class LListAddLast:
    def __init__(self):
        """ 构造空表 """

        # 表头指针  ==>  保存着这个表的首结点的引用
        # 表尾指针  ==>  保存着这个表的尾结点的引用
        # 创建空表  ==>  将表头和表尾指针设置为空链接  ==>  O(1)
        self._head = None
        self._rear = None

    def is_empty(self):
        """
        判空  ==>  O(1)  ==>  链表一般不会满，除非程序用完了可用的存储空间 """

        # 表头/表尾 指针的值是空链接 (None)  ==>  空表
        return self._head is None

    def prepend(self, elem):
        """
        头插  ==>  O(1) """

        # 创建新结点，并将其后继指向头指针
        p = LNode(elem, self._head)
        if self.is_empty():
            # 空表  ==>  表尾指针指向新结点
            self._rear = p
        # 表头指针指向新结点
        self._head = p

    def append_(self, elem):
        """
        尾插  ==>  O(1) """

        # 创建新结点，并将尾指针的后继指向该结点
        p = LNode(elem)
        self._rear.next = p
        if self.is_empty():
            # 空表  ==>  表头指针指向新结点
            self._head = p
        # 尾指针指向新结点
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

        pre = self._head
        while i > 1:          # 循环结束  ==>  pre 指向目标结点的前一结点
            i -= 1
            pre = pre.next

        # 此三步不能处理空表的情形
        # 不能处理 头插/尾插 的情形
        # pre.next = LNode(elem, pre.next)
        q = LNode(elem)
        q.next = pre.next
        pre.next = q

    def del_first(self):
        """
        删除表头结点，并返回其元素  ==>  O(1) """

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        val = self._head.elem               # 保存表首元素
        self._head = self._head.next        # 将头指针指向第二个结点
        if self._head is None:
            # 只有一个结点，尾指针要指向 None
            self._rear = None
        return val

    def del_last(self):
        """
        删除表尾结点，并返回其元素  ==>  O(n) """

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        # 只有一个元素
        if len(self) == 1:
            val = self._head.elem
            self._head = None
            self._rear = self._head
            return val

        # 不止一个元素
        val = self._rear.elem
        pre = self._head
        while pre.next.next is not None:   # 循环结束  =>  pre 是尾结点的前一个结点
            pre = pre.next
        pre.next = None                    # 不要忘记把原尾结点置 None
        self._rear = pre
        return val

    def del_all(self):
        """
        删除链表 ==> O(1) ==> 将表头指针赋值为 None (解释器的存储管理系统会自动回收不用的内存) """

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
        while i > 1:             # 循环结束  ==>  pre 指向目标结点的前一结点
            i -= 1
            pre = pre.next
        pre.next = pre.next.next

    def search_i(self, i):
        """
        按下标定位（改）  ==>  确定第 i 个元素所在结点  ==>  O(n) 尾结点可以达到 O(1) """

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
                print(' --> ', end='')
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
    llist = LListAddLast()
    llist.prepend(6)
    llist.prepend(5)
    llist.prepend(4)
    llist.prepend(3)
    llist.prepend(2)
    llist.prepend(1)
    llist.travel()

# -*- coding: utf-8 -*-
# <单链表>
# 把表中的元素分别存储在一批独立的存储块中  ==>  表的结点
# 从任一结点出发均可以找到与其相关的下一个结点 ==>  下一个关系
# 要想掌握一个单链表，只需掌握它的首结点/表头指针（如果有的话）


class LNode:
    """ 单链表结点类 """
    def __init__(self, elem, next_=None):
        # 单链表的结点类是一个二元组：(elem, next)
        # elem：保存作为表元素的数据项
        # next：保存下一个结点的标识
        self.elem = elem
        self.next = next_


class LList:
    def __init__(self):
        """ 构造空表 """
        # 表头指针  ==>  保存着这个表的首结点的引用
        # 创建空表  ==>  将表头指针设置为空链接  ==>  O(1)
        self._head = None

    def is_empty(self):
        """
        判空  ==>  O(1)  ==>  链表一般不会满，除非程序用完了可用的存储空间 """
        # 链表的结束  ==>  将表尾结点的链接域 (next) 赋值为一个不会作为结点对象标识的值  ==>  None
        # 表头指针的值是空链接 (None)  ==>  空表
        # not p  <==>  p is None
        # p      <==>  p is not None
        return self._head is None

    # 在链表中加入/删除元素时，并不需要移动已有的数据  ==>  修改链接
    def prepend(self, elem):
        """
        头插  ==>

        O(1)
                   1. 创建一个新结点，并存入数据
                   2. 把原链表首结点的链接存入新结点的连接域 (next)
                   3. 修改表头指针 _head，使之指向新结点
        """
        # 此三步可以处理空表的情形
        # self._head = LNode(elem, self._head)
        q = LNode(elem)
        q.next = self._head
        self._head = q

    def append_(self, elem):
        """
        尾插  ==>  在单链表结尾插入元素，必须先找到单链表的尾结点

        O(n)
                   1. 创建一个新结点，并存入数据
                   2. 扫描循环  =>  找到尾结点
                   3. 把新结点的链接存入尾结点的链接域 (next)
        """
        # 空表  ==>  表头指针直接指向新结点即可
        if self.is_empty():
            self._head = LNode(elem)
            return

        # 以下不能处理空表的情形
        p = self._head
        while p.next is not None:  # 循环结束  ==>  p 是尾结点
            p = p.next
        p.next = LNode(elem)

    def insert_(self, elem, i):
        """
        一般位置的插入  ==>  要想在单链表中的某位置插入一个新结点，必须先找到该位置之前的那个结点

        O(n)
                            1. 创建一个新结点，并存入数据
                            2. 扫描循环  =>  找到目标位置之前的那个结点  =>  pre
                            3. 把 pre 所指结点的 next 域的值存入新结点的链接域 next
                            4. 修改 pre 的 next 域，使之指向新结点
        """
        # 下标合法性检查
        if i < 0 or i > self.length():
            raise IndexError

        # 空表  ==>  表头指针直接指向新结点即可
        if self.is_empty():
            self._head = LNode(elem)
            return

        # 头插
        if i == 0:
            self.prepend(elem)
            return

        pre = self._head
        while i > 1:
            i -= 1
            pre = pre.next

        # 此三步不能处理空表的情形
        # 不能处理头插的情形，但可以处理尾插的情形
        # pre.next = LNode(elem, pre.next)
        q = LNode(elem)
        q.next = pre.next
        pre.next = q

    def del_first(self):
        """
        删除表头结点，并返回其元素  ==>

        O(1)
                                        1. 如果是空表，抛出异常
                                        2. 新建一个变量保存表首元素
                                        3. 将表头指针 _head 指向第二个结点
        """
        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        val = self._head.elem         # 保存表首元素
        self._head = self._head.next  # 表头指针指向第二个结点
        return val

    def del_last(self):
        """
        删除表尾结点，并返回其元素  ==>

        O(n)
                                        1. 如果是空表，抛出异常
                                        2. 扫描循环  =>  找到尾结点的前一个结点 ==>  pre
                                        3. 新建一个变量保存表尾元素
                                        4. 将表尾结点赋值为 None
        """
        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        pre = self._head
        while pre.next.next is not None:   # 循环结束  =>  pre 是尾结点的前一个结点
            pre = pre.next
        val = pre.next.elem                # 保存表尾元素
        pre.next = None
        return val

    def del_all(self):
        """
        删除链表 ==> O(1) ==> 将表头指针赋值为 None (解释器的存储管理系统会自动回收不用的内存) """
        self._head = None

    def delete_(self, i):
        """
        一般位置的删除  ==>  一般位置的删除须先找到要删除元素所在结点的前一结点

        O(n)
                             1. 扫描循环  =>  找到目标位置之前的那个结点  =>  pre
                             2. 修改 pre 的 next 域，使之指向目标结点的下一结点
        """
        # 下标合法性检查（注意，这里要 -1）
        if i < 0 or i > self.length()-1:
            raise IndexError

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

        # 头删
        if i == 0:
            self.del_first()
            return

        pre = self._head
        while i > 1:          # 循环结束  ==>  pre 是目标结点的前一结点
            i -= 1
            pre = pre.next

        # 以下不能处理头删，但可以处理尾删
        pre.next = pre.next.next

    def search_i(self, i):
        """
        按下标定位  ==>  确定第 i 个元素所在结点  ==>  O(n) """

        # 下标合法性检查（注意这里要 -1）
        if i < 0 or i > self.length()-1:
            raise IndexError

        # 空表  ==>  抛出 ValueError
        if self.is_empty():
            raise ValueError

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

    def length(self):
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
    llist = LList()
    llist.prepend(6)
    llist.prepend(5)
    llist.prepend(4)
    llist.prepend(3)
    llist.prepend(2)
    llist.prepend(1)
    llist.travel()

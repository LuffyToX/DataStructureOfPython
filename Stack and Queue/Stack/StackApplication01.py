# -*- coding: utf-8 -*-
# 栈的应用：颠倒序列 O(n)


from SequenceStack import SStack


def ListReverse(lst):
    ss = SStack()
    lst2 = list()
    for x in lst:
        ss.push(x)
    while not ss.is_empty():
        lst2.append(ss.pop_())
    return lst2


if __name__ == "__main__":
    lstOrigin = [1, 2, 3, 4, 5, 6]
    print(ListReverse(lstOrigin))

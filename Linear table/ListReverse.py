# -*- coding: utf-8 -*-
# 修改顺序表（list）自身，将其元素顺序倒置


def reverse_(lst):
    # 这里形参是列表（而不是其副本），因此修改的是列表本身
    # 这个操作的时间复杂度为 O(n)
    i, j = 0, len(lst)-1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i, j = i+1, j-1


if __name__ == "__main__":
    myList = [i for i in range(10)]
    print("倒置前：", myList)
    reverse_(myList)
    print("倒置后：", myList)
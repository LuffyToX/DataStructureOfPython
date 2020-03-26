# -*- coding: utf-8 -*-
# 简单选择排序

# 平均和最坏时间复杂度都是 O(n^2)
# 不具有适应性：任何情况下都是 O(n^2) 时间
# 不具有稳定性


from random import randint


class Item:
    def __init__(self, key, datum):
        self.key = key                             # 关键码
        self.datum = datum                         # 其余部分（不关心）

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.datum) + ")"


def selectSort(lst):
    for i in range(len(lst)-1):                    # 只需循环 n-1 次
        k = i                                      # k 是无序部分已知最小元的位置（初始为首元素）
        for j in range(i, len(lst)):               # 从无序部分的首元素开始比较
            if lst[j].key < lst[k].key:
                k = j
        if i != k:                                 # lst[k] 是确定的最小元
            lst[i], lst[k] = lst[k], lst[i]


if __name__ == "__main__":
    pathLst = list()
    for i in range(10):
        key = randint(1, 10)
        pathLst.append(Item(key, chr(65 + i)))

    print("************** 排序前 **************")
    for x in pathLst:
        print(str(x), end=' ')
    print()

    print("\n************** 排序后 **************")
    selectSort(pathLst)
    for x in pathLst:
        print(str(x), end=' ')

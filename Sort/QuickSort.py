# -*- coding: utf-8 -*-
# 快速排序


from random import randint


class Item:
    def __init__(self, key, datum):
        self.key = key                             # 关键码
        self.datum = datum                         # 其余部分（不关心）

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.datum) + ")"


def quickSortRec(lst, l, r):
    if l >= r:                                       # 分段无记录或只有一个记录
        return                                       # 说明该分段已排序
    i, j = l, r                                      # i, j 初值分别指向第一个和最后一个记录的位置
    pivot = lst[i]                                   # 记录初始空位
    while i < j:                                     # 找 pivot 的最终位置
        while i < j and lst[j].key >= pivot.key:     # 用 j 向左扫描找小于 pivot 的记录
            j -= 1                                   # 如果不满足要求，就向左移
        if i < j:                                    # 找到小于 pivot 的记录，将其移到左边的空位处
            lst[i] = lst[j]                          # 此时 j 指向的位置变成空位
            i += 1                                   # i 指向下一需要检查的记录
        while i < j and lst[i].key <= pivot.key:     # 用 i 向右扫描找大于 pivot 的记录
            i += 1                                   # 如果不满足要求，就向右移
        if i < j:                                    # 找到大于 pivot 的记录，将其移到右边的空位处
            lst[j] = lst[i]                          # 此时 i 指向的位置变成空位
            j -= 1                                   # j 指向下一需要检查的记录
    lst[i] = pivot                                   # 将 pivot 存入其最终位置
    quickSortRec(lst, l, i-1)                        # 递归处理左半区间
    quickSortRec(lst, i+1, r)                        # 递归处理右半区间


def quickSort(lst):
    quickSortRec(lst, 0, len(lst)-1)


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
    quickSort(pathLst)
    for x in pathLst:
        print(str(x), end=' ')

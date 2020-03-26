# -*- coding: utf-8 -*-
# 堆排序

# 初始建堆需要 O(n) 时间，随后每选择一个元素不超过 O(nlogn)  ==>  O(nlogn)
# 不具有稳定性
# 不具有适应性


from random import randint


class Item:
    def __init__(self, key, datum):
        self.key = key                             # 关键码
        self.datum = datum                         # 其余部分（不关心）

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.datum) + ")"


def siftdown(elems, e, begin, end):
    i, j = begin, 2*begin+1
    while j < end:
        if j+1 < end and elems[j+1].key < elems[j].key:
            j += 1
        if e.key < elems[j].key:
            break
        elems[i] = elems[j]
        i, j = j, 2*j+1
    elems[i] = e


def heapSort(lst):
    end = len(lst)
    for i in range(end//2, -1, -1):
        siftdown(lst, lst[i], i, end)
    for i in range((end-1), 0, -1):
        e = lst[i]
        lst[i] = lst[0]
        siftdown(lst, e, 0, i)


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
    heapSort(pathLst)
    for x in pathLst:
        print(str(x), end=' ')

# -*- coding: utf-8 -*-
# 插入排序

# 最坏时间复杂度 O(n^2)
# 具有适应性：如果原序列有序，只需 O(n) 时间
# 具有稳定性：在内层循环中检索插入位置的过程中，一旦发现前面的元素与当前元素关键码相等，就不再移动元素了


from random import randint


class Item:
    def __init__(self, key, datum):
        self.key = key                             # 关键码
        self.datum = datum                         # 其余部分（不关心）

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.datum) + ")"


def insertSort(lst):
    for i in range(1, len(lst)):                   # 开始时，片段 [0:1] 是有序部分
        x = lst[i]                                 # 无序部分的首元素
        j = i                                      # 每次考虑无序部分的首元素
        while j > 0 and lst[j-1].key > x.key:      # 从后往前逐个比较
            lst[j] = lst[j-1]                      # 反序逐个后移元素，确定插入位置
            j -= 1
        lst[j] = x


if __name__ == "__main__":
    pathLst = list()
    for i in range(10):
        key = randint(1, 10)
        pathLst.append(Item(key, chr(65+i)))

    print("************** 排序前 **************")
    for x in pathLst:
        print(str(x), end=' ')
    print()

    print("\n************** 排序后 **************")
    insertSort(pathLst)
    for x in pathLst:
        print(str(x), end=' ')

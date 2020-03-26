# -*- coding: utf-8 -*-
# 起泡排序

# 最坏和平均时间复杂度都是 O(n^2)
# 添加 found 标签的最好时间复杂度是 O(n)，这使算法具有了适应性
# 算法的稳定性依赖于其中相等的元素不交换


from random import randint


class Item:
    def __init__(self, key, datum):
        self.key = key                                # 关键码
        self.datum = datum                            # 其余部分（不关心）

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.datum) + ")"


def bubbleSort(lst):
    for i in range(len(lst)-1):
        found = False                                 # 是否找到逆序（默认为 False）
        for j in range(1, len(lst)-i):
            if lst[j-1].key > lst[j].key:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True                          # 找到逆序，赋值为 True
        if not found:                                 # 在一次扫描中如果没有发现逆序，就说明已排序
            break


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
    bubbleSort(pathLst)
    for x in pathLst:
        print(str(x), end=' ')

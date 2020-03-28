# -*- coding: utf-8 -*-
# 归并排序


from random import randint


class Item:
    def __init__(self, key, datum):
        self.key = key                             # 关键码
        self.datum = datum                         # 其余部分（不关心）

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.datum) + ")"


# mergeAdjacent 函数完成表中连续排放的两个有序序列的归并操作
# 被归并的有序段位于表 lfrom 中
# 归并结果存需要存入表 lto 里对应位置的分段中
# 需要归并的两个有序段分别是：lfrom[low:mid]、lto[mid:high]
# 归并结果应存入：lto[low:high]


def mergeAdjacent(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:                 # 取出两个分段中当时的最小记录
        if lfrom[i].key <= lfrom[j].key:        # lfrom[low:mid] 分段记录比 lfrom[mid:high] 小
            lto[k] = lfrom[i]                   # 将其复制到 lto 中的下一位置
            i += 1                              # lfrom[low:mid] 分段游标后移
        else:                                   # lfrom[mid:high] 分段记录比 lfrom[low:mid] 小
            lto[k] = lfrom[j]                   # 将其复制到 lto 中的下一位置
            j += 1                              # lfrom[mid:high] 分段游标后移
        k += 1
                                                # 前面循环一定会使某一个分段复制完毕
                                                # 因此以下两段循环只有一段会真正执行

    while i < mid:                              # 将 lfrom[low:mid] 分段剩余的记录复制到 lto 中
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:                             # 将 lfrom[low:mid] 分段剩余的记录复制到 lto 中
        lto[k] = lfrom[j]
        j += 1
        k += 1


# mergePass 函数实现一对对分段的一遍归并
# llen：表长度
# slen：分段长度


def mergePass(lfrom, lto, llen, slen):
    i = 0
    while (i + 2 * slen) < llen:                            # 归并长 slen 的两段
        mergeAdjacent(lfrom, lto, i, i+slen, i+2*slen)
        i += 2 * slen
    if (i + slen) < llen:                                   # 剩下两段，后段长度小于 slen
        mergeAdjacent(lfrom, lto, i, i+slen, llen)
    else:                                                   # 只剩下一段，直接复制到表 lto
        for j in range(i, llen):
            lto[j] = lfrom[j]


# mergeSort 函数是主函数
# 先安排另一个同样长度的表
# 而后在两个表之间往复地做一遍遍归并，直至完成工作


def mergeSort(lst):
    slen, llen = 1, len(lst)
    templst = [None] * llen
    while slen < llen:
        mergePass(lst, templst, llen, slen)
        slen *= 2
        mergePass(templst, lst, llen, slen)           # 结果存回原位
        slen *= 2


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
    mergeSort(pathLst)
    for x in pathLst:
        print(str(x), end=' ')

# -*- coding: utf-8 -*-
# KMP 串匹配算法


def genPnext(p):
    """ 生成针对 p 中个位置 i 的下一检查位置表，用于 KMP 算法 """

    i, k, m = 0, -1, len(p)
    pnext = [-1] * m                     # 初始数组元素全为 -1
    while i < m-1:                       # 生成下一个（即：i+1） pnext 元素值
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            pnext[i] = k                 # 设置 pnext 元素
        else:
            k = pnext[k]                 # 退到更短的前缀
    return pnext


def genPnextEnhancement(p):
    """ 生成针对 p 中个位置 i 的下一检查位置表，用于 KMP 算法 """

    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:                       # 生成下一个（即：i+1） pnext 元素值
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]                 # 退到更短的前缀
    return pnext


def KMPMatching(t, p, pnext):
    """ KMP 串匹配算法主函数 """

    i, j = 0, 0
    m, n = len(p), len(t)
    while i<m and j<n:                   # i == m 说明找到了匹配
        if i == -1 or p[i] == t[j]:      # 考虑 p 中下一个字符
            i, j = i+1, j+1
        else:                            # 匹配失败，考虑 pnext 表决定的下一字符
            i = pnext[i]
    if i == m:                           # 找到了匹配
        return j-i
    return -1


if __name__ == "__main__":
   p_str = "ABABAAABABAA"
   print(genPnext(p_str))


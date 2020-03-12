# -*- coding: utf-8 -*-
# 朴素串匹配算法


def nativeMatching(t, p):
    # t 是目标串、p 是模式串，且 m << n
    m, n = len(p), len(t)
    i, j = 0, 0
    while i<m and j<n:         # i == m 说明找到匹配
        if p[i] == t[j]:       # 字符相同，考虑下一对字符
            i, j = i+1, j+1
        else:                  # 字符不同，考虑 t 中的下一位置，且 p 回到初始位置
            i, j = 0, j-i+1
    if i == m:                 # 找到匹配，返回目标串开始下标
        return j-i
    return -1                  # 未找到匹配


if __name__ == "__main__":
    t = "abcdefghi"
    p = "ghi"
    print(nativeMatching(t, p))




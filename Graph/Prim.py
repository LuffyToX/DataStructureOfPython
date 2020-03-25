# -*- coding: utf-8 -*-
# Prim 算法（构造最小生成树）

# mst 记录所构造的最小生成树的边 ((顶点, 邻接点), 权值)
# mst[1] = ((1, 2), 10)： 顶点1∈U，且 1->2 在 mst 中
# mst[i] = None：顶点i 还不属于 U

# cands（优先队列）记录候选的最短边 (w, i, j)：i->j 侯选边的权值为 w
# 优先队列以 w 作为优先级，值较小的排在前面，w 值相同时则任选其一


from GraphBasedOnAdjacencyList import Graph
from PriorityQueueBasedOnHeap import PrioQueue


def Prim(graph):
    vnum = graph.vertexNum()
    mst = [None] * vnum
    cands = PrioQueue([(0, 0, 0)])               # 记录侯选边 (w, vi, vj)
    cnt = 0
    while cnt < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()                # 取当时的最短边
        if mst[v]:                               # 邻接点 v 已在 mst 中，进入下一次循环
            continue
        mst[v] = ((u, v), w)                     # 记录新的边和顶点
        cnt += 1
        for vi, w in graph.outEdgesList(v):      # 考虑 v 的邻接点 vi
            if not mst[vi]:                      # 如果 vi 不在 mst 中，则该边是侯选边
                cands.enqueue((w, v, vi))
    return mst


if __name__ == "__main__":
    matrix = [[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]]
    gra = Graph(matrix, 0)
    print("最小生成树：", Prim(gra))


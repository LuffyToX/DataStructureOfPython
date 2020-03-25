# -*- coding: utf-8 -*-
# Kruskal 算法（构造最小生成树）


from GraphBasedOnAdjacencyList import Graph


def Kruskal(graph):
    vnum = graph.vertexNum()
    reps = [i for i in range(vnum)]        # 代表元关系（初始时，每个顶点以自身作为代表元 reps[i]=i）
    mst, edges = list(), list()
    for vi in range(vnum):                 # 所有边加入 edges
        for v, w in graph.outEdgesList(vi):
            edges.append((w, vi, v))       # 三元组 (权, 顶点, 邻接点)
    edges.sort()                           # 按边的权值从小到大排序 O(nlogn)
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:           # 两端点属于不同的连通分量
            mst.append(((vi, vj), w))      # 记录这条边 ((顶点, 邻接点), 权值)
            if len(mst) == vnum - 1:       # |V|-1 条边，构造完成
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):          # 合并连通分量，统一代表元
                if reps[i] == orep:
                    reps[i] = rep
    return mst


if __name__ == "__main__":
    matrix = [[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]]
    gra = Graph(matrix, 0)
    print("最小生成树：", Kruskal(gra))
# -*- coding: utf-8 -*-
# 构造 DFS 生成树（递归）


from GraphBasedOnAdjacencyList import Graph


def DFSSpanForest(graph):
    vnum = graph.vertexNum()
    spanForest = [None] * vnum             # None 表示到顶点的路径尚未找到

    def DFS(grap, v):
        """ 递归遍历函数（在递归中记录经由边） """
        nonlocal spanForest                # 该 spanForest 与外部函数的 spanForest 是一个对象
        for u, w in grap.outEdgesList(v):
            if spanForest[u] is None:
                spanForest[u] = (v, w)
                DFS(grap, u)

    for ver in range(vnum):
        if spanForest[ver] is None:
            spanForest[ver] = (ver, 0)
            DFS(graph, ver)
    return spanForest


if __name__ == "__main__":
    matrix = [[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]]
    gra = Graph(matrix, 0)
    print(DFSSpanForest(gra))

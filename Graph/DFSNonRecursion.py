# -*- coding: utf-8 -*-
# DFS 非递归


from GraphBasedOnAdjacencyList import Graph
from Stack import SStack


def DFSNonRec(graph, v0):
    # 从顶点 v0 出发
    vnum = graph.vertexNum()                    # 获取定点数
    visited = [0] * vnum                        # 未访问点 0；已访问点 1
    visited[v0] = 1                             # 将初始结点 v0 标记为已访问
    seq = [v0]                                  # 记录遍历序列
    ss = SStack()
    ss.push((0, graph.outEdgesList(v0)))        # 将 (i, edges) 压栈，说明下次将访问 edges[i]
    while not ss.is_empty():
        i, edges = ss.pop_()
        if i < len(edges):
            v, e = edges[i]                     # 下次要访问的顶点，权值
            ss.push((i+1, edges))               # 下次回来将访问 points[i+1]
            if not visited[v]:                  # v 未访问，访问并记录可达点
                seq.append(v)
                visited[v] = 1
                ss.push((0, graph.outEdgesList(v)))
    return seq


if __name__ == "__main__":
    matrix = [[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]]
    gra = Graph(matrix, 0)
    print("DFS 遍历序列：", DFSNonRec(gra, 1))

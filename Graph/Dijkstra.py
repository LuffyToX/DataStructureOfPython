# -*- coding: utf-8 -*-
# Dijkstra 单源点最短路径

# 要记录到顶点 v 的最短路径，只需记录 v0 到 v 最短路径上 v 的前一顶点
# 如果对每个顶点都有了这样的记录，就可以追溯这些记录，找出从 v0 到 v 的最短路径

# paths 记录最短路径 (v', p)
# paths[v] = (v', p) 表示从顶点 v0 到 v 的最短路径上的前一顶点是 v'，该最短路径的长度是 p
# paths[v] = None 表示 v 还不在 U 里

# 求解最短路径的候选边集以路径长度作为排序码记录在优先队列 cands 中
# 队列元素形式为 (p, v, v') 表示从 v0 经 v 到 v' 的已知最短路径长度为 p
# 根据 p 的值在 cands 里的排序，保证总选出最近的未知距离顶点
# 每次选出具有最小 p 值的边，如果其终点 v' 在 V-U 中，就将其加入 paths 中
# 并将经由 v' 可达的其他顶点及其路径长度记入 cands


from GraphBasedOnAdjacencyList import Graph
from PriorityQueueBasedOnHeap import PrioQueue


def Dijkstra(graph, v0):
    vnum = graph.vertexNum()
    assert 0 <= v0 < vnum
    paths = [None] * vnum
    cnt = 0
    cands = PrioQueue([(0, v0, v0)])
    while cnt < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()                 # 取路径最短顶点
        if paths[vmin]:                                 # 如果其最短路径已知，则进入下一次循环
            continue
        paths[vmin] = (u, plen)                         # 记录新确定的最短路径
        for v, w in graph.outEdgesList(vmin):           # 考察经由新 U 顶点的路径
            if not paths[v]:                            # 是到尚为止最短路径的顶点的路径，记录
                cands.enqueue((plen+w, vmin, v))
        cnt += 1
    return paths


if __name__ == "__main__":
    matrix = [[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]]
    gra = Graph(matrix, 0)
    print("v0 的最短路径：", Dijkstra(gra, 0))
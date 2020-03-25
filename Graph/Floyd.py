# -*- coding: utf-8 -*-
# Floyd 任意顶点间最短路径


from GraphBasedOnAdjacencyMatrix import Graph


def Floyd(graph):
    inf = float("inf")
    vnum = graph.vertexNum()
    a = [[graph.getEdge(i, j) for j in range(vnum)]
         for i in range(vnum)]
    nvertex = [[-1 if a[i][j] == inf else j for j in range(vnum)]
               for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nvertex[i][j] = nvertex[i][k]
    return a, nvertex


if __name__ == "__main__":
    matrix = [[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]]
    gra = Graph(matrix, 0)

# -*- coding: utf-8 -*-
# 基于邻接表的图结构


class Graph:
    @staticmethod
    def outEdges(row, unconn):
        edges = list()
        for i in range(len(row)):
            if row[i] != unconn:
                # 确定结点的出边表 (邻接点，权值)
                edges.append((i, row[i]))
        return edges


    def __init__(self, mat=[], unconn=0):
        # 可以提供初始邻接矩阵，也可以不提供，逐步构造
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError
        # 以初始邻接矩阵生成每个顶点的出边表以构造邻接表
        # 每一个顶点的出边表都是一个列表，列表元素是一个二元组 (邻接点, 权值)
        self._mat = [self.outEdges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn


    def vertexNum(self):
        """ 获取顶点数 """
        return self._vnum


    def _invalid(self, v):
        """ 检查顶点下标的合法性 """
        return v < 0 or v >= self._vnum


    def addVertex(self):
        """ 添加顶点，并返回该顶点下标"""
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1


    def addEdge(self, vi, vj, val=1):
        """ 添加边 """
        if self._vnum == 0:
            raise ValueError
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError("顶点下标非法")

        row = self._mat[vi]                        # vi 的出边表
        i = 0
        while i < len(row):
            if row[i][0] == vj:                    # 出边表中的元素是一个二元组 (邻接点, 权值)
                self._mat[vi][i] = (vj, val)       # 修改权值
                return
            if row[i][0] > vj:                     # 原来没有到 vj 的边，退出循环后加入边
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))


    def getEdge(self, vi, vj):
        """ 获取边的权值 """
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError("顶点下标非法")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn


    def outEdgesList(self, vi):
        """ 获取指定顶点的出边表 """
        if self._invalid(vi):
            raise ValueError("顶点下标非法")
        return self._mat[vi]


if __name__ == "__main__":
    matrix = [[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]]
    gra = Graph(matrix, 0)
    print("图顶点数：%d" % gra.vertexNum())
    print("v2-v3 权值：%d" % gra.getEdge(2, 3))

    # 增加顶点
    gra.addVertex()
    print("增加顶点后的顶点数：%d" % gra.vertexNum())

    print("v3-v1 权值：%d" % gra.getEdge(3, 1))
    gra.addEdge(3, 1)
    print("v3-v1 权值：%d" % gra.getEdge(3, 1))

    print("v1 出边表：", gra.outEdgesList(1))





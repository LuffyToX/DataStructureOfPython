# -*- coding: utf-8 -*-
# 基于邻接矩阵的图结构
# 空间占用与顶点数的平方成正比
# 邻接矩阵不容易增加顶点，不太适合以逐步扩充的方式构造图对象


class Graph:
    def __init__(self, mat, unconn=0):
        # unconn 允许用户为无关联的边提供一个特殊值（默认为 0）
        # mat    初始邻接矩阵（二维表）
        vnum = len(mat)                                 # 获取行数（即：顶点数）
        for x in mat:
            if len(x) != vnum:                          # 检查是否为方阵（邻接矩阵是方阵）
                raise ValueError
        self._mat = [mat[i][:] for i in range(vnum)]    # 做拷贝
        self._unconn = unconn
        self._vnum = vnum


    def vertexNum(self):
        """ 获取顶点数 """
        return self._vnum


    def _invalid(self, v):
        """ 检查顶点下标的合法性 """
        return v < 0 or v >= self._vnum


    def addEdge(self, vi, vj, val=1):
        """ 添加边 """
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError("顶点下标非法")
        self._mat[vi][vj] = val


    def getEdge(self, vi, vj):
        """ 获取边的权值 """
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError("顶点下标非法")
        return self._mat[vi][vj]


    def outEdgesList(self, vi):
        """ 获取指定顶点的出边表 """
        if self._invalid(vi):
            raise ValueError("顶点下标非法")
        # 邻接矩阵行代表某顶点的出边
        return self.outEdges(self._mat[vi], self._unconn)


    @staticmethod
    def outEdges(row, unconn):
        edges = list()
        for i in range(len(row)):
            if row[i] != unconn:
                # 确定结点的出边表 (邻接点，权值)
                edges.append((i, row[i]))
        return edges


if __name__ == "__main__":
    matrix = [[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]]
    gra = Graph(matrix, 0)
    print("图顶点数：%d" % gra.vertexNum())
    print("v2-v3 权值：%d" % gra.getEdge(2, 3))

    print("v3-v1 权值：%d" % gra.getEdge(3, 1))
    gra.addEdge(3, 1)
    print("v3-v1 权值：%d" % gra.getEdge(3, 1))

    print("v1 出边表：", gra.outEdgesList(1))

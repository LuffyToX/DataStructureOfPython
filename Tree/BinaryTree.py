# -*- coding: utf-8 -*-
# 二叉树


from Stack import SStack
from Queue import SQueue


class BinTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data                                  # 数据域
        self.lChild = left                                # 左子树
        self.rChild = right                               # 右子树


class BinTree:
    def __init__(self, root=None):
        self.root = root


    def is_empty(self):
        return not self.root


    def binTreeCount(self, tree):
        """ 计算树中结点个数 """

        if tree is None:
            return 0
        else:
            return 1 + self.binTreeCount(tree.lChild) + self.binTreeCount(tree.rChild)

    def binTreeSum(self, tree):
        """ 树中结点数值和 """

        if tree is None:
            return 0
        else:
            return tree.data + self.binTreeSum(tree.lChild) + self.binTreeSum(tree.rChild)


    def addNode(self, elem):
        """ 添加结点：层序方式添加（完全二叉树） """

        node = BinTreeNode(elem)
        if self.root is None:                     # 如果树是空的，则对根结点赋值
            self.root = node
            return
        else:                                     # 否则通过层序遍历赋值
            que = SQueue()
            que.enqueue(self.root)                # 根结点入队
            while not que.is_empty():
                cur = que.dequeue()               # 弹出队首结点
                if cur.lChild is None:            # 先向左子结点赋值
                    cur.lChild = node
                    return
                elif cur.rChild is None:          # 后向右子结点赋值
                    cur.rChild = node
                    return
                else:                             # 如果左右孩子结点都不空，则将二者入队，进入下一层
                    que.enqueue(cur.lChild)
                    que.enqueue(cur.rChild)


    def preOrder(self, tree):
        """ 深度优先遍历：先根遍历（递归） """

        if tree is None:                             # 如果根结点为空，则为空树
            return
        print(tree.data, end=' ')                    # 打印本结点数据
        self.preOrder(tree.lChild)                   # 遍历左子树（递归）
        self.preOrder(tree.rChild)                   # 遍历右子树（递归）


    def preOrderNonRec(self, tree):
        """ 深度优先遍历：先根遍历（非递归） """

        ss = SStack()
        while tree or not ss.is_empty():
            while tree:
                # yield tree.data                    # 改为生成器
                print(tree.data, end=" ")            # 打印本结点数据
                ss.push(tree.rChild)                 # 右子树入栈
                tree = tree.lChild                   # 沿左子树下行
            tree = ss.pop_()                         # 遇到空树，回溯


    def midOrder(self, tree):
        """ 深度优先遍历：中根遍历（递归）"""

        if tree is None:                          # 如果根结点为空，则为空树
            return
        self.midOrder(tree.lChild)                # 遍历左子树（递归）
        print(tree.data, end=" ")                 # 打印本结点数据
        self.midOrder(tree.rChild)                # 遍历右子树（递归）


    def midOrderNonRec(self, tree):
        """ 深度优先遍历：中根遍历（非递归） """

        ss = SStack()
        while tree or not ss.is_empty():
            while tree:
                ss.push(tree)                     # 将根结点入栈
                tree = tree.lChild                # 沿左子树下行
            tree = ss.pop_()                      # 遇到空树，回溯
            # yield tree.data                     # 改为生成器
            print(tree.data, end=" ")             # 打印当前结点数据
            tree = tree.rChild


    def postOrder(self, tree):
        """ 深度优先遍历：后根遍历（递归） """

        if tree is None:                          # 如果根结点为空，则为空树
            return
        self.postOrder(tree.lChild)               # 遍历左子树（递归）
        self.postOrder(tree.rChild)               # 遍历右子树（递归）
        print(tree.data, end=" ")                 # 打印本结点数据


    def postOrderNonRec(self, tree):
        """ 深度优先遍历：后根遍历（非递归） """

        ss = SStack()
        while tree or not ss.is_empty():
            while tree:                                              # 下行循环
                ss.push(tree)                                        # 将根结点入栈
                tree = tree.lChild if tree.lChild else tree.rChild   # 能左就左
            tree = ss.pop_()                                         # 栈顶为应访问的结点
            # yield tree.data                                        # 改为生成器
            print(tree.data, end=" ")                                # 打印本结点数据
            if not ss.is_empty() and ss.top().lChild == tree:
                tree = ss.top().rChild                   # 栈不空且当前结点是栈顶的左子结点
            else:
                tree = None                              # 没有右子树或右子树遍历完毕，强迫退栈


    def breadthFirstSearch(self):
        """ 广度优先遍历（BFS）也称层序遍历 """

        que = SQueue()
        que.enqueue(self.root)                      # 根结点入队
        while not que.is_empty():
            cur = que.dequeue()                     # 弹出队首结点
            print(cur.data, end=" ")                # 打印当前数据
            if cur.lChild:
                que.enqueue(cur.lChild)             # 左子结点入队
            if cur.rChild:
                que.enqueue(cur.rChild)             # 右子结点入队


if __name__ == "__main__":
    t = BinTree()
    for x in [10, 5, 12, 4, 7, 8, 14, 87, 99]:
        t.addNode(x)
    print("************* 先根遍历 **************")
    t.preOrder(t.root)
    print()
    t.preOrderNonRec(t.root)
    print()

    print("************* 中根遍历 **************")
    t.midOrder(t.root)
    print()
    t.midOrderNonRec(t.root)
    print()

    print("************* 后根遍历 **************")
    t.postOrder(t.root)
    print()
    t.postOrderNonRec(t.root)
    print()

    print("************* BFS **************")
    t.breadthFirstSearch()
    print()

    print("树中结点个数为：%d" % t.binTreeCount(t.root))
    print("树中结点数值和为： %d" % t.binTreeSum(t.root))



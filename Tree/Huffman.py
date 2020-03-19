# -*- coding: utf-8 -*-
# 哈夫曼树


from PriorityQueueBasedOnHeap import PrioQueue


class HuffmanTreeNode:
    """ 哈夫曼树结点类 """

    def __init__(self, data, left=None, right=None):
        self.data = data                                  # 数据域
        self.lChild = left                                # 左子树
        self.rChild = right                               # 右子树


    def __lt__(self, other):
        return self.data < other.data


class HuffmanPrioQueue(PrioQueue):
    """ 专门为哈夫曼树服务的优先队列类 """

    def __init__(self):
        super().__init__()


    def number(self):
        return len(self._elems)


def HuffmanTree(widget):
    """ 找到哈夫曼树顶权：widget 权 """

    tQueue = HuffmanPrioQueue()                            # 哈夫曼优先队列
    for w in widget:
        tQueue.enqueue(HuffmanTreeNode(w))                 # 哈夫曼树结点入队（小堆顶）
    while tQueue.number() > 1:
        t1 = tQueue.dequeue()                              # 最小权
        t2 = tQueue.dequeue()                              # 次小权
        x = t1.data + t2.data
        tQueue.enqueue(HuffmanTreeNode(x, t1, t2))         # 将二者和加入优先队列
    return tQueue.dequeue()                                # 最终对垒中只剩下哈夫曼树树顶权


if __name__ == "__main__":
    widgets = [2, 3, 7, 10, 4, 2, 5]
    print(HuffmanTree(widgets).data)


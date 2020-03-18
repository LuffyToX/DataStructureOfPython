# 二叉树和树

树形结构由结点和结点之间的连接关系构成，最重要的特征包括：

+ 一个结构如果不空，其中就存在着唯一的起始结点，称为 **树根**
+ 树根外的其余结点都有且只有一个前驱、一个结点可以有 0 个或多个后继
+ 结构里的所有结点都在树根结点通过后继关系可达的结点集合里
+ 结点之间的联系不会形成循环关系（结点之间的联系形成了一种序，但一般不像线性表那样形成一个全序）





## 二叉树：概念和性质

二叉树是一种最简单的树形结构：

+ 树中每个结点至多关联到两个后继结点，即：一个结点的关联结点数可以是 0、1、2
+ 一个结点关联的后继结点明确的分左右：**左关联结点**、**右关联结点**





### 二叉树的概念

二叉树是结点的有穷集合。这个集合或者是空集，或者其中有一个称为根节点的特殊结点，其余结点分属两棵不相交的二叉树，这两棵二叉树分别是原二叉树的左子树和右子树。显然，这是一种递归定义：一棵二叉树可能有两棵子树，其子树也是二叉树，结构与整棵树相同

对于非空二叉树，其结点集合非空，至少包含一个根节点，但其子树可以为空（两棵子树都可以为空）

二叉树的两棵子树有明确的左右之分，讨论子树时必须明确说明是左子树还是右子树

不包含任何结点的二叉树称为 **空树**；只包含一个结点的二叉树称为 **单点树**

一棵二叉树的根结点称为该树的子树根结点的 **父结点**；子树的根结点称为二叉树树根结点的 **子结点**（相对关系）；父结点相同的两个结点称为 **兄弟结点**

可以认为从父结点的子结点有一条连线，称为从父结点到子结点的边，注意，这种边有方向，形成一种单方向的父子关系。基于父子关系可以定义其传递关系，称为祖先子孙关系

在二叉树里，有些结点的两棵子树都空（没有子结点），这种结点称为 **树叶**，树中其余结点称为 **分支结点**。分支结点可以只有一个分支，对于二叉树，只有一个分支时必须说明它是其左分支还是右分支

一个结点的子结点个数称为该结点的 **度数**：

+ 树叶结点度数为 0
+ 分支结点度数为 1 或 2

一棵二叉树只有 5 种可能的形态：

1. 空二叉树
2. 单点树（只有根结点）
3. 只有根结点和左子树
4. 只有根结点和右子树
5. 两棵子树俱全



从一个祖先结点到其任何子孙结点都存在一系列边，形成从前者到后者的联系。这样一系列首尾相连的边称为树中的 **一条路径**，路径中边的条数称为该路径的 **长度**。从一棵二叉树的根结点到该树中的任一结点都有路径且唯一

二叉树是一种层次结构：

+ 规定二叉树根的层次为 0
+ 对位于 $k$ 层的结点，其子结点是 $k+1$ 层的元素

则从树根到树中任一结点的路径长度就是该结点所在的层数，也称为该结点的 **层数**

一棵二叉树的高度（也称为深度）就是树中结点的最大层数（也就是这棵树里的最长路径的长度）





### 二叉树的性质

作为数据结构，二叉树最重要的性质就是树的高度和树中可以容纳的最大结点个数之间的关系：

+ 在长为 $n$ 的表里只能容纳 $n$ 个结点
+ 在高为 $h$ 的二叉树中可以容纳 $2^{h+1}-1$ 个结点



满二叉树：如果二叉树中所有分支结点的度数都是 $2$，则称它为一棵满二叉树

扩充二叉树：对二叉树 $T$，加入足够多的新叶结点，使 $T$ 的原有结点都变成度数为 $2$ 的分支结点，得到的二叉树称为 $T$ 的扩充二叉树。扩充二叉树中新增的结点称为其外部结点，原树 $T$ 的结点称为其内部结点

完全二叉树：对于一棵高度为 $h$ 的二叉树，如果其 $0$ 层至第 $h-1$ 层的结点都满，并且如果最后一层的结点不满，则所有结点在最左边连续排列（空位都在右边），这样的二叉树称为 完全二叉树



**性质1**：在非空二叉树第 $i$ 层中至多有 $2^i$ 个结点

**性质2**：高度为 $h$ 的二叉树至多有 $2^{h+1}-1$ 个结点

**性质3**：对于任何非空二叉树 $T$，如果其叶结点个数为 $n_0$，度数为 $2$ 的结点个数为 $n_2$，那么 $n_0=n_2+1$

**性质4**：满二叉树的叶结点比分支结点多一个

**性质5**：任何二叉树的扩充二叉树都是满二叉树，扩充二叉树的外部结点个数比内部结点个数多 $1$

**性质6**：扩充二叉树的外部路径长度 $E$ 是从树根到树中各外部结点的路径长度之和，内部路径长度 $I$ 是从树根到树中各内部结点的路径长度之和。如果该树有 $n$ 个内部结点，那么 $E=I+2\times n$

**性质7**：$n$ 个结点的完全二叉树的高度 $h=[log_2n]$（不大于 $log_2n$ 的最大整数）

**性质8**：如果 $n$ 个结点的完全二叉树的结点按层次并按从左到右的顺序从 $0$ 开始编号，对任一结点 $i$：

+ 根节点序号为 $0$
+ 对于 $i>0$：其父结点的编号为 $(i-1)/2$
+ 若 $2i+1<n$：其左子结点序号为 $2i+1$，否则它无左子结点
+ 若 $2i+2<n$：其右子结点序号为 $2i+2$，否则它无右子结点



一般而言，对于 $n$ 个结点的二叉树有如下情况：

+ 如果它足够 “丰满整齐”（如：完全二叉树），最长路径长度将为 $O(logn)$
+ 如果它比较 “畸形”，最长路径长度可能达到 $O(n)$





### 二叉树的抽象数据类型

首先，结点是二叉树的基础，通常主要用结点保存于应用有关的信息

此外，作为二叉树的表示，还需要记录二叉树的结构信息，至少需要保证能检查结点的父子关系

```python
ADT BinTree:
    BinTree(self, data, left, right)     # 构造空二叉树
    is_empty(self)                       # 判断 self 是否为一个空二叉树
    num_nodes(self)                      # 求二叉树的结点个数
    data(self)                           # 获取二叉树根节点存储的数据
    left(self)                           # 获取二叉树的左子树
    right(self)                          # 获取二叉树的右子树
    set_left(self, btree)                # 用 btree 取代原来的左子树
    set_right(self, btree)               # 用 btree 取代原来的右子树
    elements(self)                       # 遍历二叉树中各结点数据的迭代器
    travel(self, op)                     # 对二叉树中每个结点的数据执行 op 操作
```





### 遍历二叉树

每棵二叉树都有唯一的根结点，可以将其看作这棵二叉树的唯一标识，是基于树结构的处理过程的入口。从根结点出发应该能找到树中的所有信息，其基础是从父结点找到两个子结点，因此，实际中常用根结点代表这棵二叉树

遍历一棵二叉树就是按某种系统化的方式访问二叉树里的每个结点一次：

+ 深度优先遍历：顺着一条路径尽可能向前探索，必要时回溯（检查完一个叶结点，由于无路可走，只能回头）
+ 广度优先遍历：在所有路径上齐头并进





#### 深度优先遍历

按深度优先方式遍历一棵二叉树，需要做三件事：遍历左子树（$L$）、遍历右子树（$R$）、访问根结点（$D$）

选额这三项工作的不同执行顺序，就可以得到三种常见的遍历顺序（假设总是先处理左子树）：

1. 先根遍历（$DLR$）  ==>  先根序列
2. 中根遍历（$LDR$）  ==>  中根序列（也称对称序列）
3. 后根遍历（$LRD$）  ==>  后根序列



给定了一棵二叉树的任意一种遍历序列，都无法唯一确定相应的二叉树

如果知道了一棵二叉树的对称序列，又知道另一遍历序列（无论先根还是后根），就可以唯一确定这棵二叉树





#### 广度优先遍历

广度优先是按路径长度由近到远地访问结点，即：逐层访问树中各结点（这种遍历不能写成一个递归过程）

在广度优先遍历中只规定了逐层访问，并没有规定同一层结点地访问顺序。但从算法地角度看，必须规定一个顺序，常见的是在每一层里都从左到右逐个访问。实现这一算法需要用一个队列作为缓存

广度优先遍历又称为按层次顺序遍历，这样遍历产生的结点序列称为二叉树地层次序列





## 基于 $list$ 的二叉树简单实现

简单看，二叉树结点也就是一个三元组，元素是左右子树和本结点数据（$list$ 和 $tuple$ 的区别仅在于变动性）

二叉树是递归结构，$Python$ 的 $list$ 也是递归结构，基于 $list$ 类型很容易实现二叉树：

+ 空树用 $None$ 表示
+ 非空二叉树用包含三个元素的表 $[d, l, r]$ 表示（[根结点元素，左子树，右子树]）

显然，这样做把二叉树映射到一种分层的 $list$ 结构，每棵二叉树都有与之对应的 $list$，如：

```python
# 将同一层的子树相互对齐，便于阅读

['A', ['B', None, None],
      ['C', ['D', ['F', None, None],
                  ['G', None, None]],
            ['E', ['H', None, None],
                  ['I', None, Noe]]]]
```



```python
def BinTree(data, left=None, right=None):
    return [data, left, right]


def root(btree):
    return btree[0]


def left(btree):
    return btree[1]


def right(btree):
    return btree[2]


def setRoot(btree, data):
    btree[0] = data
    

def setLeft(btree, left):
    btree[1] = left

    
def setRight(btree, right):
    btree[2] = right
   

if __name__ == "__main__":
    tree = BinTree(2, BinTree(4), BinTree(8))
```





## 优先队列

从原理上说，这种结构与二叉树没有直接关系，但是基于对一类二叉树的认识，可以做出优先队列的一种高效实现

作为缓存结构，优先队列与栈和队列类似，可以将元素保存其中，可以访问和弹出

优先队列的特点是存入其中的每项数据都另外附有一个数值，表示这个项的优先程度，称为其 **优先级**：

+ 优先队列应该保证，在任何时候访问和弹出的，总是当时在这个结构里保存的所有元素中优先级最高的
+ 如果不止一个元素的优先级最高，优先队列将保证访问或弹出的是它们中的一个，具体由内部实现确定

抽象的看，需要缓存的是一个有序集 $S=(D, \leq)$ 的元素，其中 $\leq$ 是集合 $D$ 上的一个全序，表示元素的优先关系





### 基于线性表的优先队列

数据项在线性表里的存储顺序可用于表示优先级关系（两种实现方式）：

1. 存入数据时，保证表中元素始终按优先顺序排列
2. 存入数据时采用最简单的方式（顺序表表尾，链接表表头），取用时通过检索找到最优元素

采用线性表实现优先队列，无论采用怎样具体的实现技术，在插入元素与取出元素之间总有一种是 $O(n)$

> - 顺序表 + 方式一
> - 顺序表 + 方式二
> - 链接表 + 方式一
> - 链接表 + 方式二





### 树形结构和堆

采用前面讨论的实现，按序插入操作低效，其根源就在于需要沿着表顺序检索插入位置。这说明，只要元素按优先级顺序线性排列，就无法避免线性复杂性问题：

+ 对于顺序表：需要移动 $O(n)$ 个元素
+ 对于链接表：需要顺着链接爬行 $O(n)$ 步

如果不改变数据的线性顺序存储方式，就不可能突破 $O(n)$ 的复杂度限制



从结构上看，堆就是结点里存储数据的完全二叉树，但堆中数据的存储要满足一种特殊的堆序：在一个结点里所存的数据先于或等于其子结点（如果有的话）里的数据

+ 在一个堆中，从树根到任何一个叶结点的路径上，各结点里所存的数据按规定的优先关系（非严格）递减
+ 堆中最优先的元素必定位于二叉树的根结点里（堆顶），$O(1)$ 时间就可以取得
+ 位于树中不同路径上的元素，这里不关心其顺序关系



**小堆顶**：堆中每个结点里的数据均小于或等于其子结点的数据（小元素优先）

**大堆顶**：堆中每个结点里的数据均大于或等于其子结点的数据（大元素优先）



堆与完全二叉树有下面几个重要性质：

+ 在堆的最后加上一个元素，整个结构还是可以看作一棵完全二叉树，但它未必是堆（最后元素未必满足堆序）
+ 去掉堆顶后其余元素形成两个子堆，完全二叉树的子结点/父结点下标计算规则仍适用，堆序在路径上仍成立
+ 给两个子堆加入一个根元素，得到的结点序列又可看作完全二叉树，但它未必是堆（根结点未必满足堆序）
+ 去掉堆中最后的元素（最下层的最后结点），剩下的元素仍构成一个堆





### 基于堆的优先队列

用堆作为优先队列，可以直接得到堆中的最优元素 $O(1)$ 时间，但还要解决两个问题：

- 如何实现插入元素操作：向堆中加入一个新元素，必须能够得到一个包含了所有原有元素和刚加入元素的堆
- 如何实现弹出元素操作：从堆中弹出最小元素后，必须能够把剩余元素重新做成堆

这两个操作均可在 $O(logn)$ 时间内完成



现在基于前面的认识定义一个优先队列类，在这个类对象里，还是用一个 $list$ 存储元素

+ 在表尾加入元素
+ 以首端作为堆顶























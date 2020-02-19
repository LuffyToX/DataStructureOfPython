## 线性表的抽象数据类型：

```python
ADT List:
    List(self)                            # 表构造操作，创建一个新表
    is_empty(self)                        # 判断 self 是否为一个空表
    len_(self)                            # 获得 self 的长度
    prepend(self, elem)                   # 将元素 elem 加入表中作为第一个元素
    append_(self, elem)                   # 将元素 elem 加入表中作为最后一个元素
    insert_(self, elem, i)                # 将元素 elem 加入表中作为第 i 个元素，其它元素顺序不变
    del_first(self)                       # 删除表中的首元素
    del_last(self)                        # 删除表中的尾元素
    del_(self, i)                         # 删除表中第 i 个元素
    search(self, elem)                    # 查找元素 elem 在表中出现的位置，不出现时返回 -1
    forall(self, op)                      # 对表中的每个元素执行 op 操作
```



## 顺序表










































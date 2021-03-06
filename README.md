# Python 数据结构与算法

计算机具有通用性，其本身的功能很简单，就是能执行程序，按程序的指示完成一系列操作，得到某些结果，或者产生某些效果。要想用计算机处理一个具体问题，就需要有一个解决该问题的程序



一般而言，人们需要的不是解决一个具体问题的程序，而是解决一类问题的程序，如：

> 一个文本编辑器不应该只能编辑出一个具体的文本文件，而应该能用于编辑各种文本文件
>
> Python 解释器不应该只能执行一个具体的 Python 程序，而是可以执行所有可能的 Python 程序



人们设计开发一个程序，通常是为了解决一个问题，该程序的每次执行能处理该问题的一个实例：

+ 开发者针对要解决的问题开发出相应的程序
+ 使用者运行程序处理问题的具体实例，完成具体计算



程序开发就是根据面对的问题，最终得到一个可以解决问题的程序的工作过程。真正的问题来自实际，是不清晰和不明确的，而程序是对计算机操作过程的精确描述，两者之间有着非常大的距离，因此，一般而言，程序开发工作需要经过一系列工作阶段才能完成，由于人的认识能力的限制，其中还可能出现反复

+ 分析阶段

  > 实际中提出的问题往往是模糊的，缺乏许多细节，是一种含糊的需求。因此，程序开发的第一步就是深入分析问题，弄清其方方面面的情况和细节，将问题严格化，最终得到一个比较详尽的尽可能严格表述的问题描述。在软件开发领域，这一工作通常被称为需求分析

+ 设计阶段

  > 在真正编程之前需要有一个能解决这个问题的计算过程模型，这种模型需要包括两个方面：
  >
  > + 表示计算中处理的数据（数据结构）
  > + 求解的计算方法（算法）

+ 编码阶段

  > 有了解决问题的抽象计算模型，下一步的工作就是采用某种适当的编程语言实现这个模型，即：编程

+ 检查编译阶段

  > 复杂的程序往往不能一蹴而就，写出的代码可能有各种错误，通过反复检查修改，得到可以运行的程序

+ 测试/调试阶段

  > 程序可以运行并不代表它就是所需的那个程序，还需要通过尝试性的运行确定其功能是否得到满足



考虑一个计算问题时，需要注意到三个重要概念：

+ 问题

  > 一个问题 $W$ 是需要解决的一个具体需求

+ 问题实例

  > 问题 $W$ 的一个实例 $w$ 是该问题的一个具体实例

+ 算法

  > 解决问题 $W$ 的一个算法 $A$ 是对一种计算过程的严格描述



对于算法的理论研究应该具有一定的抽象性，需要做出一些简单假设：

+ 所用的计算设备中为数据存储准备了一组基本单元，每个单元只能保存固定的一点有限数据
+ 机器能执行一些基本操作，计算中的一次操作消耗一个单位的时间



在算法和数据结构领域，人们最常用的是下面这组渐进复杂度函数：

+ $O(1)$                   常量复杂度
+ $O(logn)$             对数复杂度
+ $O(n)$                  线性复杂度
+ $O(nlogn)$
+ $O(n^2)$                平方复杂度
+ $O(n^3)$                立方复杂度
+ $O(2^n)$                指数复杂度
+ $O(n^n)$



考虑最基本的循环程序，其中只有顺序组合、条件分支和循环结构：

+ 基本操作：

  > 认为其时间复杂度为 $O(1)$，如果是函数调用，应该将其时间复杂度代入，参与整体时间复杂度的计算

+ 加法规则（顺序复合）

  > 如果算法是两个（或多个）部分的顺序复合，其复杂性是这两个（或多个）部分的复杂性之和，如：
  > $$
  > T(n)=T_1(n)+T_2(n)=O(T_1(n))+O(T_2(n))=O(max(T_1(n)，T_2(n)))
  > $$

+ 乘法规则（循环结构）

  > 如果算法是一个循环，循环体将执行 $T_1(n)$ 次，每次执行需要 $T_2(n)$ 时间，那么：
  > $$
  > T(n)=T_1(n)\times T_2(n)=O(T_1(n))\times O(T_2(n))=O(T_1(n)\times T_2(n))
  > $$

+ 取最大规则（分支结构）

  > 如果算法是条件分支，两个分支的时间复杂度分别为 $T_1(n)$ 和 $T_2(n)$，那么：
  > $$
  > T(n)=O(max(T_1(n)，T_2(n)))
  > $$



在程序中使用一种数据结构，有两层映射：

+ 把这种结构映射到编程语言提供的基本数据机制中，这一映射称为（抽象）数据结构的物理实现

  > 上层实现牵涉到有效利用语言提供的各种数据机制

+ 编程语言系统（编译器 / 解释器）将把通过语言的数据机制定义的数据结构映射到计算机存储器中

  > 底层实现牵涉到有效利用计算机的存储器



内存的基本结构是线性排列的一批存储单元，每个单元的大小相同，可以保存一个单位大小的数据，具体单元大小可能因计算机的不同而有所不同，内存单元具有唯一的编号，称为地址。在程序执行中，对内存单元的访问都通过单元的地址进行，因此，要访问一个内存单元，必须先掌握其地址

> 基于地址访问内存单元是一个 $0(1)$ 操作，与单元的位置或整个内存的大小无关（这样的存储器称作 $RAM$）

为了表示程序中的一个对象，需要在当时空闲的内存中确定一块或几块区域（地址连续排列的内存单元），把该对象的数据存入其中。在程序运行中，建立对象时需要安排存储，还有许多与对象存储和使用有关的管理工作，解释器的存储管理系统负责这些工作，这一工作是自动进行的，并且，当一个对象不再有用时，存储管理系统也会设法回收其占用的存储，以便在将来用于存储其它对象。一个程序在运行中将不断建立一些对象并使用它们，建立的每个对象都有一个确定的唯一标识，用于识别和使用这个对象

> 在一个对象的存续期间，其标识保持不变，这也是一个基本原则，如：
>
> Python 标准函数 $id$ 取得对象的标识，内置操作 $is$ 和 $is$ $not$ 通过比较标识的方式判断是否为同一个对象

在具体系统中用什么作为对象标识，是系统设计者的考虑和选择，最简单的方式就是直接使用对象的内存地址



在计算机内存中表示数据元素之间的关系，只有两种基本技术：

+ 利用数据元素的存储位置隐式表示

  > 顺序表示

+ 把数据元素之间的联系也看作一种数据，显示地保存在内存中

  > 链接表示



高级语言里的变量是内存及其地址的抽象，变量本身也需要在内存中安排位置，每个变量占用若干存储单元

在 Python 中，可以通过初始化给变量约束一个值，还可以通过赋值修改变量的值

> 这里的值就是对象，给变量约束一个对象，就是把该对象的标识存入该变量
>
> 从变量出发访问其值是常量时间操作，这是 Python 里分析程序的时间代价的基础

Python  变量的值都是对象，可以是基本整数、浮点数等类型的对象，也可以是组合类型的对象。程序中建立和使用的各种复杂对象，都基于独立的存储块实现，通过链接相互关联。程序里的名字（变量、参数、函数名等）关联着作为其值的对象，这种关联可以用赋值操作改变（这种实现方式称为引用语义）

+ 引用语义

  > 变量所需的存储空间大小一致，因为其中只需要保存一个引用

+ 值语义：

  > 一个整数类型的变量就需要保存一个整数所需的空间
  >
  > 一个浮点数类型的变量就需要保存一个浮点数所需的空间
  >
  > $\cdots$

需要把这种结构映射到编程语言提供的基本数据机制中，这一映射称为（抽象）数据结构的物理实现；编程语言
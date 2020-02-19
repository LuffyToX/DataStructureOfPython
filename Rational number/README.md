## 有理数抽象数据类型：

```bash
ADT Rational:                               # 定义有理数的抽象数据类型
    Rational(int num, int den)              # 构造有理数 mun/den
    +(Rational r1, Rational r2)             # 求出表示 r1+r2 的有理数
    -(Rational r1, Rational r2)             # 求出表示 r1-r2 的有理数
    *(Rational r1, Rational r2)             # 求出表示 r1*r2 的有理数
    /(Rational r1, Rational r2)             # 求出表示 r1/r2 的有理数
    num(Rational r)                         # 求出有理数 r 的分子
    den(Rational r)                         # 求出有理数 r 的分母
```




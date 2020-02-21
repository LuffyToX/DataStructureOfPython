# -*- coding: utf-8 -*-
# 有理数类


class Rational:
    @staticmethod
    def _gcd(m, n):
        """ 求最大公约数  ==>  欧几里得算法 """
        # 0 可以被任意非零整数整除              =>  任意非零整数都是 0 的约数
        # 任意整数和 0 的约数是该整数的所有约数  =>  最大公约数是该整数本身
        # 1. n=0 and m!=0  =>  m, n 交换  =>  return m
        # 2. m=0 and n!=0  =>  return m
        # 3. 其它情况       =>  gcd(m, n) = gcd(n, m%n) ... 当 n=0 时对应的 m 就是最大公约数
        if m == 0:
            m, n = n, m
        while n != 0:
            # 不必考虑 m, n 孰大孰小  ==>  gcd(10, 15) = gcd(15, 10) = gcd(10, 5) = gcd(5, 0) = 5
            m, n = n, m%n

        return m

    def __init__(self, num, den=1):
        """ 在初始化有理数时，就进行了约分 """
        # num => 分子
        # den => 分母
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError

        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -num, -sign

        g = Rational._gcd(num, den)
        self._num = sign * (num//g)
        self._den = sign * (den//g)

    def num(self): return int(self._num)

    def den(self): return int(self._den)

    def plus(self, another):
        num = self._num * another.den() + self._den * another.num()
        den = self._den * another.den()

        return Rational(num, den)

    def subtract(self, another):
        num = self._num * another.den() - self._den * another.num()
        den = self._den * another.den()

        return Rational(num, den)

    def multiply(self, another):
        num = self._num * another.num()
        den = self._den * another.den()

        return Rational(num, den)

    def divide(self, another):
        num = self._num * another.den()
        den = self._den * another.num()

        return Rational(num, den)


if __name__ == "__main__":
    r1 = Rational(3, 5)
    r2 = Rational(7, 15)
    result_plu = r1.plus(r2)
    result_sub = r1.subtract(r2)
    result_mul = r1.multiply(r2)
    result_div = r1.divide(r2)

    print("%d/%d +  %d/%d = %d/%d" % (r1.num(), r1.den(), r2.num(), r2.den(), result_plu.num(), result_plu.den()))
    print("%d/%d -  %d/%d = %d/%d" % (r1.num(), r1.den(), r2.num(), r2.den(), result_sub.num(), result_sub.den()))
    print("%d/%d *  %d/%d = %d/%d" % (r1.num(), r1.den(), r2.num(), r2.den(), result_mul.num(), result_mul.den()))
    print("%d/%d // %d/%d = %d/%d" % (r1.num(), r1.den(), r2.num(), r2.den(), result_div.num(), result_div.den()))

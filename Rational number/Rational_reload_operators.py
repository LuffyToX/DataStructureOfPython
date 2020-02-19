# -*- coding: utf-8 -*-


class Rational:
    @staticmethod
    def _gcd(m, n):
        """ 求最大公约数  ==>  欧几里得算法 """
        if m == 0:
            m, n = n, m
        while n != 0:
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

    # 算数运算
    def __add__(self, other):
        """ +  """
        return Rational(self._num * other.den() + self._den * other.num(), self._den * other.den())

    def __sub__(self, other):
        """ - """
        return Rational(self._num * other.den() - self._den * other.num(), self._den * other.den())

    def __mul__(self, other):
        """ * """
        return Rational(self._num * other.num(), self._den * other.den())

    def __floordiv__(self, other):
        """ // """
        return Rational(self._num * other.den(), self._den * other.num())

    # 逻辑运算
    def __eq__(self, other):
        """ == """
        return self._num * other.den() == self._den * other.num()

    def __ne__(self, other):
        """ != """
        return self._num * other.den() != self._den * other.num()

    def __lt__(self, other):
        """ < """
        return self._num * other.den() < self._den * other.num()

    def __le__(self, other):
        """ <= """
        return self._num * other.den() <= self._den * other.num()

    def __gt__(self, other):
        """ > """
        return self._num * other.den() > self._den * other.num()

    def __ge__(self, other):
        """ >= """
        return self._num * other.den() != self._den * other.num()

    # 输出
    def __str__(self):
        """ str() """
        return str(self._num) + '/' + str(self._den)


if __name__ == "__main__":
    r1 = Rational(3, 5)
    r2 = Rational(7, 15)

    print("%s + %s = %s" % (str(r1), str(r2), str(r1+r2)))
    print("%s - %s = %s" % (str(r1), str(r2), str(r1-r2)))
    print("%s * %s = %s" % (str(r1), str(r2), str(r1*r2)))
    print("%s // %s = %s" % (str(r1), str(r2), str(r1//r2)))


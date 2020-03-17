# -*- coding: utf-8 -*-
# 栈的应用：括号匹配问题


from SequenceStack import SStack


class BracketsMatching:
    def __init__(self, text):
        self.text = text
        self.brackets = "()[]{}"                           # 所有括号字符
        self.openBrackets = "([{"                          # 所有开括号字符
        self.pairs = {')': '(', ']': '[', '}': '{'}        # 表示配对关系的字典

    def genBracket(self):
        """ 括号生成器，每次调用返回 text 里的下一括号及其位置 """

        i, textLen = 0, len(self.text)
        while True:
            while i < textLen and self.text[i] not in self.brackets:
                i += 1
            if i >= textLen:
                return
            yield self.text[i], i
            i += 1

    def Matching(self):
        """ 括号配对主函数 """

        ss = SStack()                                                 # 保存开括号的栈
        for br, i in self.genBracket():                               # 对 text 里各括号和位置迭代
            if br in self.openBrackets:                               # 开括号，压栈并继续
                ss.push(br)
            elif ss.pop_() != self.pairs[br]:                         # 不匹配就是失败，退出
                print("Unmatching is found at %d for %s" %(i, br))
                return False
            else:                                                     # 匹配成功，什么也不做
                pass
        print("All btackets are correctly matched")
        return True


if __name__ == "__main__":
    textOrigin = "[(1+1)*5+6]*5+6*(1-3)"
    bm = BracketsMatching(textOrigin)
    bm.Matching()

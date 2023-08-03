class Solution:
    def solve(self, digits, arr):
        if not digits:
            return [""]

        c = digits[0]
        a = arr[int(c)]
        small_input = digits[1:]
        rest = self.solve(small_input, arr)
        res = []
        for x in rest:
            for x1 in a:
                res.append(x1 + x)
        return res

    def __init__(self):
        self.ans = []

    def solve2(self, digits, arr, i, com):
        if i == len(digits):
            self.ans.append(com)
            return

        c = digits[i]
        a = arr[int(c)]
        for x1 in a:
            self.solve2(digits, arr, i + 1, com + x1)

    def letterCombinations(self, digits):
        a = []
        if not digits:
            return a
        arr = ["0", "0", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.solve2(digits, arr, 0, "")
        return self.ans


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        c = 0
        for k, v in enumerate(operations):
            if v == '+':
                res.append(res[c - 1] + res[c - 2])
                c += 1
            elif v == 'C':
                res.pop()
                c -= 1
            elif v == 'D':
                res.append(2 * res[c - 1])
                c += 1
            else:
                res.append(int(v))
                c += 1
            print(res)
        
        return sum(res)
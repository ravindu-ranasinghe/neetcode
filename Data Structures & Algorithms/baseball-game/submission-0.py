class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stak = []
        for x in operations:
            if x == '+':
                if len(stak) >=2:
                    stak.append(stak[-1]+stak[-2])
            elif x == 'D':
                if len(stak) >=1:
                    stak.append(stak[-1] * 2)
            elif x == "C":
                if len(stak) >= 1:
                    stak.pop()
            else:
                stak.append(int(x))
        return sum(stak)


        
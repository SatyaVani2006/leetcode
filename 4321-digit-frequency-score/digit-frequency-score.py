from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        digits=str(n)
        freq=Counter(digits)
        sum=0
        for d,f in freq.items():
            sum+=int(d)*f
        return sum    

        
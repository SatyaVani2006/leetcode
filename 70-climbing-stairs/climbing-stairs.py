class Solution:
    def climbStairs(self, n: int) -> int:
        #if n <= 2: return n
        #first, second = 1, 2
        #for _ in range(3, n + 1):
          # first, second = second, first + second
        #return second
        if n==1:
            return 1
        if n==2:
            return 2
        prev=1
        curr=2
        for i in range(2,n):
            prev,curr=curr,curr+prev
        return curr            

        
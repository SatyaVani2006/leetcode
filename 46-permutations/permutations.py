class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # prem=permutations(nums)
        # return list(prem)
        res=[]
        sol=[]
        n=len(nums)
        def backtrack():
            if len(sol)==n:
                res.append(sol[::])
                return
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return res                
        
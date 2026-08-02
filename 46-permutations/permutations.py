class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        prem=permutations(nums)
        return list(prem)
        
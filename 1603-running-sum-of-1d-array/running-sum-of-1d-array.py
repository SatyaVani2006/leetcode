class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        total = 0
        for n in nums:
            total += n
            ans.append(total)
        return ans
        
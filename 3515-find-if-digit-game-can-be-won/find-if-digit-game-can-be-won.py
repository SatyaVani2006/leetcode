class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        count1=0
        count2=0
        for num in nums:
            if num<10:
                count1+=num
            else:
                count2+=num
        if count1==count2:
            return False
        else:
            return True

        
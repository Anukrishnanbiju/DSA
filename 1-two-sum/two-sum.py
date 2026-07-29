class Solution:
    def twoSum(self, nums: list[int],target: int) ->list[int]:
        PrevMap = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in PrevMap:
                return[PrevMap[diff],i]
            PrevMap[n]=i
        return 
    
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for j in range(len(nums)):
            sol = target - nums[j]
            if sol in hashmap and j != hashmap[sol]:
                return [ j, hashmap[sol]]

        


        
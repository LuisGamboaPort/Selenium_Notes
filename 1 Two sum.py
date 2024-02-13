from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                result = [prevMap[diff], i]
                print("Result:", result)
                return result
            prevMap[n] = i
        print ("No two elements found.")
        return []

nums_list = [2,1,5,3]
target_value = 4
solution = Solution()
solution.twoSum(nums_list,target_value)


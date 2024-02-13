

class Solution:
    test_nums = [1,2,3,1]
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

sol = Solution()

print(sol.containsDuplicate(sol.test_nums))

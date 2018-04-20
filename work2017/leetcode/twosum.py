class Solution(object):
    def twoSum(self, nums, target):
        while nums != []:
            i = nums.pop()
            if target-i in nums:
                return [nums.index(target-i), len(nums)]

if __name__ == '__main__':
   a = Solution()
   b = a.twoSum([2, 7, 11, 15], 26)
   print b
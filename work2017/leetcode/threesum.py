class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        # if len(nums) < 3:
        #     return answer
        # else:
        #     for i in range(len(nums) - 1):
        #         b = nums[i] + nums[i+1]
        #         if -b in nums and nums.index(-b) != i and nums.index(-b) != i+1:
        #             l1 = sorted([nums[i], nums[i+1], -b])
        #             if l1 not in answer:
        #                 answer.append(l1)
        #     return answer
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    ident = nums[left] + nums[right] + nums[i]
                    if ident == 0:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1; right -= 1
                        while left < right and nums[left] == nums[left-1]:    # skip duplicates
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif ident < 0:
                        left += 1
                    else:
                        right -= 1
        return ans

if __name__ == '__main__':
    S = Solution()
    print S.threeSum([-1, 0, 1, 2, -1, -4])
    print S.threeSum([0, 0])
    print S.threeSum([0, 0, 0])
    print S.threeSum([0, 0, 0, 0])
    print S.threeSum([3, -2, 1, 0])


def twoSum(nums, target):
	while nums != []:
		i = nums.pop()
		if target-i in nums:
			#print(target-i)
			return [nums.index(target-i),len(nums)]

print(twoSum([3,2,4],6))
print(twoSum([0,3,4,0],0))
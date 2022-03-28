'''

1. 2 <= nums.length <= 104
2. -109 <= nums[i] <= 109
3. -109 <= target <= 109
4. Only one valid answer exists.
5. less than O(n)^2

in: (set of numbs,target_value)
out: (num_set[x] + num_set[y] == target)
solve: {
  for x,
  for y
}

psuedocode:
num_set = []
target = int

for x in num_set:
  for y in num_set:
    if x + y == target:
      v1 = num_set.index(x)
      v2 = num_set.index(y)
      return [v1,v2]

apparently hash tables are more efficient

'''
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
      complement = target - nums[i]
      if complement in hashmap:
        return [i, hashmap[complement]]
      hashmap[nums[i]] = i
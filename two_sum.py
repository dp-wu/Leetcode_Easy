# Use fast-slow pointers


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        slow = 0
        while slow < length:
            fast = slow + 1
            while fast < length:
                if nums[slow] + nums[fast] == target:
                    return [slow, fast]
                fast += 1
            slow += 1

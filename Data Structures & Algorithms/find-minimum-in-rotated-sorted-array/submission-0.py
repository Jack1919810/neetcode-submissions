class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1       # mid 在左段(高段),最小值在右边
            else:
                right = mid          # mid 在右段(低段),最小值在 mid 或其左
        return nums[left]
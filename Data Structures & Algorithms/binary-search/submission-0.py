class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1      # target 在右半,丢掉 mid 及左边
            else:
                right = mid - 1     # target 在左半,丢掉 mid 及右边
        return -1
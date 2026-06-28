class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 判断哪半有序
            if nums[left] <= nums[mid]:        # 左半有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1            # target 在有序左半
                else:
                    left = mid + 1
            else:                              # 右半有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1             # target 在有序右半
                else:
                    right = mid - 1
        return -1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是较短的,二分在短数组上做
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2      # 左半要放的元素个数
        
        left, right = 0, m           # 在 nums1 上切的位置 i 的范围 [0, m]
        while left <= right:
            i = (left + right) // 2  # nums1 左半取 i 个
            j = half - i             # nums2 左半取 j 个(被 i 决定)
            
            # 四条边界,越界时用 ±无穷兜底
            L1 = nums1[i-1] if i > 0 else float('-inf')   # 左1最右
            R1 = nums1[i]   if i < m else float('inf')    # 右1最左
            L2 = nums2[j-1] if j > 0 else float('-inf')   # 左2最右
            R2 = nums2[j]   if j < n else float('inf')    # 右2最左
            
            if L1 <= R2 and L2 <= R1:
                # 完美切割!
                if total % 2 == 1:
                    return max(L1, L2)            # 奇数:左半最大值
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2  # 偶数
            elif L1 > R2:
                right = i - 1        # nums1 左边切多了,i 调小
            else:                    # L2 > R1
                left = i + 1         # nums1 左边切少了,i 调大
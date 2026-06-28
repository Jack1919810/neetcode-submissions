class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum((p + k - 1) // k for p in piles)
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid          # mid 可行,但可能还有更小的,保留 mid
            else:
                left = mid + 1       # mid 太慢,必须更快
        return left
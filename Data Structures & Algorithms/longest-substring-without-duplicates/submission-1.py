class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in seen:      # 右指针撞到重复
                seen.remove(s[l])    # 从左边挤出去
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)  # 当前窗口长度
        return res
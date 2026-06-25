class Solution:
    def minWindow(self, s: str, t: str) -> str:
            need = {}
            for c in t:
                need[c] = need.get(c, 0) + 1
            missing = len(t)          # 还差多少个字符(含重复)

            left = 0
            best = ""
            for right, c in enumerate(s):
                if need.get(c, 0) > 0:
                    missing -= 1
                need[c] = need.get(c, 0) - 1   # 可以变负,表示窗口里多余的量

                while missing == 0:
                    if not best or right - left + 1 < len(best):
                        best = s[left:right + 1]
                    need[s[left]] += 1
                    if need[s[left]] > 0:      # 从负/零回到正,说明缺了
                        missing += 1
                    left += 1
            return best
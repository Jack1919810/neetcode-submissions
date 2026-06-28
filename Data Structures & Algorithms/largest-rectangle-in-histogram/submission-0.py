class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # 每个元素是 (start_index, height)
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            # 栈顶比当前矮的柱子,在这里"结算"它的最大矩形
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx  # 关键:当前柱子可以接着它的位置往左延伸
            stack.append((start, h))
        # 处理栈里剩下的:它们一直延伸到数组末尾
        n = len(heights)
        for idx, height in stack:
            max_area = max(max_area, height * (n - idx))
        return max_area
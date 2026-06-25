class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()      # 存下标,nums[下标] 单调递减
        res = []
        for i, n in enumerate(nums):
            # 不变量1:弹掉队尾比当前小的
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(i)
            # 不变量2:队首过期就弹
            if dq[0] <= i - k:
                dq.popleft()
            # 第一个完整窗口形成后开始记录
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
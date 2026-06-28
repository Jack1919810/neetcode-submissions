from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)   # key -> [(timestamp, value), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        # 找最后一个 timestamp <= 目标的元素
        left, right = 0, len(arr) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]     # 这个可行,记下来,继续往右找更大的合法时间戳
                left = mid + 1
            else:
                right = mid - 1       # 时间戳太大,往左找
        return res
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        cur_time = 0.0  # 当前最前方车队的到达时间
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > cur_time:
                # 追不上前面的车队,自己成立新车队
                fleets += 1
                cur_time = time
            # else: time <= cur_time,被前面车队"吸收",不新增
        return fleets
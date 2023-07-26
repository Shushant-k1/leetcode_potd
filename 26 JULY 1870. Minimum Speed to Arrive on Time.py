class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def canReach(s):
            return sum([ceil(d / s) for d in dist[:-1]], 0) + dist[-1] / s <= hour
        
        lo, hi = 1, 10 ** 7
        min_speed = -1
        while lo <= hi:
            speed = (hi - lo) // 2 + lo
            if canReach(speed):
                min_speed = speed
                hi = speed - 1
            else:
                lo = speed + 1
        return min_speed

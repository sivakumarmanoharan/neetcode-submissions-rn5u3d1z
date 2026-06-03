from collections import deque

class HitCounter:

    def __init__(self):
        self.queue = deque()
        self.total_count = 0

    def hit(self, timestamp: int) -> None:
        if self.queue and self.queue[-1][0] == timestamp:
            self.total_count +=1
            self.queue[-1] = (timestamp, self.queue[-1][1]+1)
        else:
            self.queue.append((timestamp,1))
            self.total_count +=1

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0][0] >= 300: 
            old = self.queue.popleft() 
            self.total_count -= old[1] 
        return self.total_count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

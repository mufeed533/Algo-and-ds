"https://leetcode.com/problems/design-underground-system/description/"

class UndergroundSystem:

    def __init__(self):
        self.metrics = {}
        self.journies = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.journies:
            self.journies[id] = (stationName, t)        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.journies:
            startStation, start_time = self.journies[id]
            if (startStation, stationName) not in self.metrics:
                self.metrics[(startStation, stationName)] = [0, 0]
            
            total_journies, total_timings = self.metrics[(startStation, stationName)]
            total_journies += 1
            total_timings += (t - start_time)
            self.metrics[(startStation, stationName)] = [total_journies, total_timings]
            del self.journies[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_journies, total_timings = self.metrics[(startStation, endStation)]
        if not total_timings or not total_journies:
            return 0
        return total_timings / total_journies
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # 1. Check if the new event conflicts with any double-booked intervals
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        
        # 2. Find new double-bookings by checking against single-booked intervals
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))
                
        # 3. Accept the booking safely
        self.calendar.append((start, end))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
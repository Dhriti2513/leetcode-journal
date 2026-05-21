class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        exclusive_times = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fn_id_str, event, timestamp_str = log.split(':')
            fn_id = int(fn_id_str)
            timestamp = int(timestamp_str)
            
            if event == "start":
                if stack:
                    exclusive_times[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:
                exclusive_times[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
                
        return exclusive_times

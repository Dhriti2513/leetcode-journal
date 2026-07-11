class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
        queue = deque()
        visited_routes = set()
        for route_idx in stop_to_routes[source]:
            queue.append((route_idx, 1))
            visited_routes.add(route_idx)
        while queue:
            route_idx, bus_count = queue.popleft()
            for stop in routes[route_idx]:
                if stop == target:
                    return bus_count
                for next_route_idx in stop_to_routes[stop]:
                    if next_route_idx not in visited_routes:
                        visited_routes.add(next_route_idx)
                        queue.append((next_route_idx, bus_count + 1))
        return -1
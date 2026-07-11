class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        queue = deque([id])
        visited = {id}
        dist = 0
        
        while queue and dist < level:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for neighbor in friends[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            dist += 1
        video_freq = Counter()
        for friend_id in queue:
            for video in watchedVideos[friend_id]:
                video_freq[video] += 1
        result = sorted(video_freq.keys(), key=lambda x: (video_freq[x], x))
        
        return result
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph) - 1
        results = []

        def dfs(curr_node, path):
            if curr_node == target:
                results.append(list(path))
                return

            for neighbor in graph[curr_node]:
                path.append(neighbor)  
                dfs(neighbor, path)   
                path.pop()

        dfs(0, [0])
        return results
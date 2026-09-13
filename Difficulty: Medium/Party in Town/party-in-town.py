class Solution:
    def bfs(self, adj, start):
        n = len(adj)
        dist = [-1] * n
        q = deque()
    
        dist[start] = 0
        q.append(start)
    
        farthest_node = start
        farthest_dist = 0
    
        while q:
            node = q.popleft()
    
            for next_node in adj[node]:
    
                # Convert 1-based house number
                # to 0-based index.
                next_node -= 1
    
                if dist[next_node] == -1:
    
                    dist[next_node] = dist[node] + 1
                    q.append(next_node)
    
                    # Update the farthest house.
                    if dist[next_node] > farthest_dist:
                        farthest_dist = dist[next_node]
                        farthest_node = next_node
    
        return farthest_node, farthest_dist
    
    def partyHouse(self, adj: list[list[int]]) -> int:
            diameter_end, _ = self.bfs(adj, 0)

            # Second BFS:
            # Find the diameter length.
            _, diameter = self.bfs(adj, diameter_end)

            # The optimal party house lies at the center
            # of the diameter.
            # ceil(diameter / 2) = (diameter + 1) // 2
            return (diameter + 1) // 2

import heapq
class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        adj = [[] for _ in range(n + 1)]
        # Create adjacency list with both directions.
        for edge in edges:
            u = edge[0]
            v = edge[1]

            # Original direction requires no reversal.
            adj[u].append([v, 0])

            # Reverse direction requires one reversal.
            adj[v].append([u, 1])

        # Store the minimum reversals required to reach each node.
        dist = [float('inf')] * (n + 1)

        # Priority queue stores {distance, node}.
        pq = []

        # Distance of source is 0.
        dist[src] = 0
        heapq.heappush(pq, (0, src))

        # Apply Dijkstra's algorithm.
        while pq:
            d, node = heapq.heappop(pq)

            # Skip outdated entries.
            if d != dist[node]:
                continue

            # Explore all adjacent nodes.
            for edge in adj[node]:
                next = edge[0]
                cost = edge[1]

                # Update the distance if a better path is found.
                if d + cost < dist[next]:
                    dist[next] = d + cost
                    heapq.heappush(pq, (dist[next], next))

        # No path exists from src to dst.
        if dist[dst] == float('inf'):
            return -1

        return dist[dst]
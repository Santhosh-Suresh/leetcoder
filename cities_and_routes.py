##Reorder Routes to Make All Paths Lead to the City Zero

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0

        edges_to = dict().fromkeys(range(n))
        edges_from = dict().fromkeys(range(n))

        for i in range(n):
            edges_to[i] = set()
            edges_from[i] = set()

        for edge in connections:
            edges_from[edge[0]].add(edge[1])
            edges_to[edge[1]].add(edge[0])

        stack = [0]
        visited = set()
        #         print(edges_from)
        #         print(edges_to)

        while stack:
            curr_node = stack.pop(0)
            visited.add(curr_node)
            stack.extend(list(edges_to[curr_node] - visited))
            ans += len(edges_from[curr_node] - visited)
            stack.extend(list(edges_from[curr_node] - visited))

        return ans
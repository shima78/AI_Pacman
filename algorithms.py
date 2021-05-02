from HW1.maps import Map
import time
import heapq
import math


class Search:

    def __init__(self):
        self.count = 4

    def dfs(self, m: Map) -> list:
        start_time = time.time()
        start = m.me
        goals = m.goals
        ls = []

        stack = [(start, [start])]
        visited = []
        for g in goals:
            ls.append(g)

        while stack and ls:
            vertex, path = stack[-1]
            stack.pop()

            if vertex in ls:
                ls.remove(vertex)

            if vertex not in visited:
                visited.append(vertex)
                for node in m.get_successors(vertex[0], vertex[1]):
                    if node not in visited:
                        stack.append((node, path + [node]))
        print('depth first Search')
        print('Duration:', time.time() - start_time)

        return visited

    def bfs(self, m: Map) -> list:
        start_time = time.time()
        start = m.me
        goals = m.goals
        ls = []
        queue = [(start, [start])]
        visited = []
        for g in goals:
            ls.append(g)
        while queue and ls:
            vertex, path = queue.pop(0)
            if vertex in ls:
                ls.remove(vertex)

            if vertex not in visited:
                visited.append(vertex)
                for node in m.get_successors(vertex[0], vertex[1]):
                    if node not in visited:
                        queue.append((node, path + [node]))
        print('breadth first Search')
        print('Duration:', time.time() - start_time)

        return visited

    def uniform_cost(self, m: Map) -> list:
        start_time = time.time()
        start = m.me
        goals = m.goals
        ls = []
        p = []
        fringe = [(0, start, [start])]
        visited = []

        for g in goals:
            ls.append(g)
        # ls is the list of on visited goals
        while fringe and ls:
            # fringe is a priority queue , extracts the node with least cost
            cost, vertex, path = heapq.heappop(fringe)

            # remove goal
            if vertex in ls:
                ls.remove(vertex)

            if vertex not in visited:
                visited.append(vertex)
                for node in m.get_successors(vertex[0], vertex[1]):
                    heapq.heappush(fringe, (cost + 1, node, path + [node]))

        print('Uninformed Search')
        print('Duration:', time.time() - start_time)
        # return path_node
        return visited

    def get_euclidean_heuristics(self, a, m:Map ) -> list:
        goals = m.goals
        h = []
        for g in goals:
            dist = math.sqrt(math.pow((a[0] - g[0]), 2) + math.pow((a[1] - g[1]), 2))
            h.append(dist)

        return h

    def a_star(self, m: Map, heuristics: list) -> list:
        start_time = time.time()
        start = m.me
        goals = m.goals
        ls = []
        for g in goals:
            ls.append(g)
        # (f ,(cost,h), node, path)
        fringe = [(
            min(self.get_euclidean_heuristics(m.me, m))
            , (0, min(self.get_euclidean_heuristics(m.me, m)))
            , start, [start]
        )]

        visited = []

        while fringe and m.goals:
            # extract the node with least F value
            current_f, cost_h, vertex, path = heapq.heappop(fringe)
            # check if we reached a goal
            if vertex in m.goals:
                # remove goal
                m.goals.remove(vertex)
                # start over from this goal to find other near goals
            if vertex not in visited:
                visited.append(vertex)
                for node in m.get_successors(vertex[0], vertex[1]):
                    if node not in visited and m.goals:
                        # increase cost at each level
                        c = cost_h[0] + 1
                        # find nearest goal cost
                        h = min(self.get_euclidean_heuristics(node, m))
                        f = c + h
                        heapq.heappush(fringe, (f, (c, h), node, path + [node]))
        for l in ls:
            m.goals.append(l)
        print('A* Search')
        print('Duration:', time.time() - start_time)

        return visited

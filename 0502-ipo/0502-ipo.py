class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        projects = list(zip(capital, profits))
        projects.sort(key=lambda x: x[0])

        max_heap = []
        index = 0

        for _ in range(k):
            while index < len(projects) and projects[index][0] <= w:
                heapq.heappush(max_heap, -projects[index][1]) 
                index += 1

            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w
        
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def gain(passed, total):
            return (passed + 1) / (total + 1) - passed / total
        
        maxHeap = []
        for passed, total in classes:
            heapq.heappush(maxHeap, (-gain(passed, total), passed, total))
        
        
        while extraStudents > 0:
            _, passed, total = heapq.heappop(maxHeap)
            passed += 1
            total += 1
            extraStudents -= 1
            heapq.heappush(maxHeap, (-gain(passed, total), passed, total))
            
        total_ratio = 0
        for _, passed, total in maxHeap:
            total_ratio += passed / total

        return total_ratio / len(classes)
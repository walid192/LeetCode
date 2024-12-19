class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 1

        sorted_arr = sorted(arr)
        chunks = 0

        running_sum_original = 0
        running_sum_sorted = 0

        for i in range(len(arr)):
            running_sum_original += arr[i]
            running_sum_sorted += sorted_arr[i]

            if running_sum_original == running_sum_sorted:
                chunks += 1

        return chunks

from collections import Counter
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = Counter(arr1)
        result = []

        for num in arr2:
            result.extend([num] * count[num])
            del count[num]

        remaining_elements = sorted(count.elements())
        result.extend(remaining_elements)

        return result

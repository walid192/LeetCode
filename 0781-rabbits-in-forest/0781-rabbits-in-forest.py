class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        cnt=collections.Counter(answers)
        res=0

        for key,value in cnt.items():
            group_size = key + 1 
            groups = math.ceil(value/group_size)
            res += groups * group_size
        return res
        
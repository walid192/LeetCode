class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = [0 if (nums[i] % 2 != nums[i - 1] % 2) else 1 for i in range(1, len(nums))]
        
        prefix_res = [0] * (len(res) + 1)
        for i in range(1, len(prefix_res)):
            prefix_res[i] = prefix_res[i - 1] + res[i - 1]
        
        answer = []
        for fromi, toi in queries:
            if fromi == toi: 
                answer.append(True)
            else:
                invalid_count = prefix_res[toi] - prefix_res[fromi]
                if invalid_count > 0:
                    answer.append(False)
                else:
                    if (nums[fromi] % 2 == nums[fromi + 1] % 2) or (nums[toi - 1] % 2 == nums[toi] % 2):
                        answer.append(False)
                    else:
                        answer.append(True)
        
        return answer
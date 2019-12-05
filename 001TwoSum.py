class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            req_num = target - nums[i]
            if req_num in num_dict:
                return num_dict[req_num], i
            num_dict[nums[i]]=i

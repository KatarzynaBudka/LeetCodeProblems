class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = 0
        min_len = float('inf')
        i = 0
        for k in range(len(nums)):
            cur_sum += nums[k]
            while cur_sum >= target:
                if k-i+1<min_len:
                    min_len = k-i+1
                cur_sum-=nums[i]
                i+=1
        return min_len if min_len !=float('inf') else 0


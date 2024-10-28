class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}
        i=0
        while i <len(nums):
            if nums[i] not in num_count.keys():
                num_count[nums[i]] = 1
            else:
                num_count[nums[i]] +=1
            if num_count[nums[i]] > 2:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
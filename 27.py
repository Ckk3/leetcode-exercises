from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        original_list = nums.copy()
        numbers_removed = 0
        for num in original_list:
            if num == val:
                numbers_removed += 1
                nums.remove(num)

        [nums.append('_') for x in range(numbers_removed)]
        
        k = len(nums) - numbers_removed

        print(nums)
        print(k)

        return k




test_class = Solution()
test_class.removeElement(nums=[0,1,2,2,3,0,4,2], val=2)

from typing import List
from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        awnser = []
        prod_calculated = {}
        for x in range(len(nums)):
            if nums[x] in prod_calculated.keys():
                awnser.append(prod_calculated[nums[x]])
                continue

            current_nums = nums.copy()
            current_value = current_nums.pop(x)
            current_result = prod(current_nums)
            awnser.append(current_result)
            prod_calculated[current_value] = current_result


        return awnser


test_class = Solution()
print(test_class.productExceptSelf(nums=[1,2,3,4]))

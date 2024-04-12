from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = 0
        map_numbers = {}
        
        for num in nums:
            try:
                map_numbers[num] += 1
            except KeyError:
                map_numbers[num] = 1

        map_calculated = {}
        for key, value in map_numbers.items():
            map_calculated[value / 2] = key

        print(map_calculated[max(map_calculated)])
        return map_calculated[max(map_calculated)]





test_class = Solution()
test_class.majorityElement(nums=[3,2,3])
test_class.majorityElement(nums=[2,2,1,1,1,2,2])
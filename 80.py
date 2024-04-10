from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        original_list = nums.copy()
        duplicated_numbers = {}
        numbers_removed = 0

        for num in original_list:
            if num in duplicated_numbers.keys():
                if duplicated_numbers[num] >= 2:
                    numbers_removed += 1
                    nums.remove(num)
                    continue
            try:
                duplicated_numbers[num] += 1
            except KeyError:
                duplicated_numbers[num] = 1

        [nums.append('_') for x in range(numbers_removed)]
        
        k = len(nums) - numbers_removed

        print(nums)
        print(k)

        return k



test_class = Solution()
test_class.removeDuplicates(nums=[1,1,1,2,2,3])
test_class.removeDuplicates(nums=[0,0,1,1,1,1,2,3,3])
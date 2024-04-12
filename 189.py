from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        for i in range(k):
            # print(f"current list {nums}")
            current_number = nums[-1]
            del(nums[-1])
            nums.insert(0, current_number)
    
        print(f"last list {nums}")






test_class = Solution()
test_class.rotate(nums=[1,2,3,4,5,6,7], k=3)

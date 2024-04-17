from typing import List

class Solution:
    # def canJump(self, nums: List[int]) -> bool:
        
    #     current_index = 0
    #     max_index = len(nums) - 1

    #     return self.check_if_can_go_to_finish(current_index, max_index, nums)


    # def check_if_can_go_to_finish(self, current_index, max_index, nums):
    #     if current_index >= max_index:
    #         return True
        
    #     try:
    #         current_jumps = nums[current_index]
    #     except IndexError:
    #         return True
        
    #     try:
    #         nums[current_index + current_jumps]
    #     except IndexError:
    #         return True

    #     if current_jumps == 0:
    #         return False
        
    #     for jump in range(1, current_jumps + 1):
    #         if self.check_if_can_go_to_finish(current_index=current_index + jump, max_index=max_index, nums=nums) is False:
    #             continue
    #         return True

    #     return False

    def canJump(self, nums: List[int]) -> bool:
        # using @frestre solution because i'm dumb as fck https://leetcode.com/problems/jump-game/solutions/4534808/super-simple-intuitive-8-line-python-solution-beats-99-92-of-users
        
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True




test_class = Solution()
print(test_class.canJump(nums=[2,3,1,1,4])) # True
print(test_class.canJump(nums=[3,2,1,0,4])) # False
print(test_class.canJump(nums=[2,5,0,0])) # True
print(test_class.canJump(nums=[2,0,0])) # True
print(test_class.canJump(nums=[5,9,3,2,1,0,2,3,3,1,0,0])) # True
print(test_class.canJump(nums=[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6])) 
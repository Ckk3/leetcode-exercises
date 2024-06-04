from typing import List

# Using thelinuxman solution
class Solution:
    def trap(self, height: List[int]) -> int:
        mh = max(height)
        block_vol = sum(height)

        left = 0
        max_left = 0
        while height[left] < mh:
            if height[left] > max_left:
                max_left = height[left]
            
            height[left] = max_left
            left += 1
        
        right = len(height)-1
        max_right = 0
        while height[right] < mh:
            if height[right] > max_right:
                max_right = height[right]
            
            height[right] = max_right
            right -= 1
        
        filled_vol = sum(height[0:left]+height[right:]) + (right-left)*mh
        return filled_vol - block_vol



solution = Solution()
print(solution.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(solution.trap(height=[4,2,0,3,2,5])) # 9
print(solution.trap(height=[5,4,1,2])) # 1
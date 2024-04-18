from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        jump_quantity = 0
        last_index = len(nums) - 1
        index_to_ignore = []

        for index, n in enumerate(nums):
            if index in index_to_ignore:
                continue

            if index == last_index:
                break

            if (index + n) >= last_index:
                jump_quantity += 1
                break


            try:
                all_next_values = [(value, nums[index + value]) for value in range(1, n + 1)]
                # print(all_next_values)
            except IndexError:
                # print("Chegou ao fim")
                break
            
            best_next_index = max(all_next_values, key=lambda x: x[0] + x[1])[0] + index
            # print(best_next_index)
            for next_values in all_next_values:
                new_index = index + next_values[0]
                if new_index == best_next_index:
                    break
                index_to_ignore.append(new_index)
                # print(index_to_ignore)

            jump_quantity += 1
        
        return jump_quantity




test_class = Solution()
print(test_class.jump(nums=[2,3,1,1,4])) # 2
print(test_class.jump(nums=[2,3,0,1,4])) # 2
print(test_class.jump(nums=[7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])) # 2
print(test_class.jump(nums=[0])) # 0
print(test_class.jump(nums=[1])) # 0
print(test_class.jump(nums=[2,1])) # 1
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1[:m]
        # nums2 = nums2[:n]
        # nums1.extend(nums2)

        list_with_all_numbers = nums1[:m] + nums2[:n]
        min_number = min(list_with_all_numbers)
        index_to_substitute = 0
        while True:
            for number in list_with_all_numbers:
                if number == min_number:
                    nums1[index_to_substitute] = number
                    list_with_all_numbers.remove(number)
                    index_to_substitute += 1

            if len(list_with_all_numbers) == 0:
                break

            min_number = min(list_with_all_numbers)

        # for x in range(len(new_list)):
        #     nums1[x] = new_list[x]
        print(nums1)

test = Solution()
test.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n = 3)
test.merge(nums1=[0], m=0, nums2=[1], n = 1)
test.merge(nums1=[0,0,3,0,0,0,0,0,0], m=3, nums2=[-1,1,1,1,2,3], n = 6)
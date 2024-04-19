from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # I use @Kashyap_Gohil solution to fix this code
        # https://leetcode.com/problems/h-index/solutions/4928640/python-2-approaches-sorting-counting-summary-with-comparison/?envType=study-plan-v2&envId=top-interview-150
        
        citations.sort()

        articles_total = len(citations)

        
        for index, c in enumerate(citations):
            if (articles_total - index) <= c:
                return (articles_total - index)
        
        return 0



test_class = Solution()
print(test_class.hIndex(citations=[3,0,6,1,5])) # 3 
print(test_class.hIndex(citations=[1,3,1])) # 1 
print(test_class.hIndex(citations=[1])) # 1
print(test_class.hIndex(citations=[0])) # 0
print(test_class.hIndex(citations=[1,2,2])) # 2
print(test_class.hIndex(citations=[100])) # 1
print(test_class.hIndex(citations=[11,15])) # 2
print(test_class.hIndex(citations=[4,4,0,0])) # 2

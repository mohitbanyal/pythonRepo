"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(target,num):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    left = 0
    right = 1
    print(len(num))
    while(left<len(num)):
        while right < len(num):
            if num[left]+num[right] == target :
                return(left,right)
            else:
                right = right+1
    left=left+1

print(twoSum(6,[3,2,3]))
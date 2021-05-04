'''
Shangjun Jiang
CS 5001, Fall 2020
Lab 14 -- frequency_sort
'''


def sort(nums):
    '''
    Function -- sort
        sort the given nums by frequency
    Parameters:
        nums -- an unordered list
    Do change on the initial list
    '''

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            count1 = nums.count(nums[i])
            count2 = nums.count(nums[j])
            if count1 < count2:
                nums.insert(i, nums[j])
                del nums[j + 1]

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            num1 = nums[i]
            num2 = nums[j]
            if num1 == num2:
                nums.insert(i, nums[j])
                del nums[j + 1]
    return nums

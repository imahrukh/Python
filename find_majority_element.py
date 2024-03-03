def find_majority_element(nums):
    a = -1
    b = 0
    for c in range (len(nums)):
        if b == 0:
            a = nums[c]
            b = 1
        elif a == nums[c]:
            b = b + 1
        else :
            b = b - 1
    return a

if __name__ == '__main__':
    nums = [2, 3 , 2, 1, 4, 2, 2, 4]
    print('the majority element is' , find_majority_element(nums))
    
    

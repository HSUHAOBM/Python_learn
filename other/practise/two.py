nums = [1, 5, 6, 9, 11, 12]
target = 15

def twoSum(nums, target):

    d = {}

    for index,value in enumerate(nums):
        print(index, value)
        # if(target-value in d):
        #     return(d[target-value],index)
        # else:
        #     d[value] = index

print(twoSum(nums, target))
print(enumerate(nums).__dict__)
def two_sum(nums, target):
    h = {}
    pos = 0
    while pos < len(nums):
        if(target-nums[pos]) not in h:
            h[nums[pos]] = pos
            pos += 1
            print(h)
        else:
            return [h[target-nums[pos]], pos]

#loops
"""
48 ms
nums = [2,15,11,7]
target = 9
{2: 0}
{2: 0, 15: 1}
{2: 0, 15: 1, 11: 2}
[0, 3]
"""

def two_sum2(nums, target):
    h = {}
    result = []
    for index, comp in enumerate(nums):
        if comp not in h:
            h[target-comp] = index
            print(h)
        else:
            result = [h[comp], index]
    return result

"""
nums = [2,15,11,7]
target = 9
{7: 0}
{7: 0, -6: 1}
{7: 0, -6: 1, -2: 2}
[0, 3]
"""


def two_sum3(nums, target):
    h = {}
    pos = 0
    while pos < len(nums):
        comp = target - nums[pos]
        if(target-comp) not in h:
            h[comp] = pos
            pos += 1
            print(h)
        else:
            return [h[target-comp], pos]

"""
44ms faster than 85% 
nums = [2,15,11,7]
target = 9

{7: 0}
{7: 0, -6: 1}
{7: 0, -6: 1, -2: 2}
[0, 3]
"""



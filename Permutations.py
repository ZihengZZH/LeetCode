'''

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

# Simple iterative algorithm
def permute(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i]+[n]+perm[i:])
        perms = new_perms
    return perms
    

def permute_online(nums):
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in permute_online(nums[1:])
                     for i in range(len(nums))] or [[]]
        

if __name__ == "__main__":
    input = [1,2,3,4]
    output = permute(input)
    print("OUTPUT",output)


'''
[[1]]
[[2,1], [1,2]]
[[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]]
...........
'''
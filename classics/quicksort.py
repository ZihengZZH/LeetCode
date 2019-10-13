import random

'''
Standard implementation
'''
def partion(inputs, left, right):
    pivot = inputs[(left+right) // 2]
    while left <= right:
        while inputs[right] > pivot:
            right -= 1
        while inputs[left] < pivot:
            left += 1
        if left <= right:
            tmp = inputs[left]
            inputs[left] = inputs[right]
            inputs[right] = tmp
            left += 1
            right -= 1
    return left

def quick_sort(inputs, left, right):
    pivot_index = partion(inputs, left, right)
    if left < pivot_index - 1:
        quick_sort(inputs, left, pivot_index - 1)
    if pivot_index < right:
        quick_sort(inputs, pivot_index, right)

inputs = [2,3,8,4,9,5,6,5,6,10,17,11,2]
quick_sort(inputs, 0, len(inputs) - 1)
print(inputs)

'''
Pythonic implementation
'''
def qsort(inputs):
    if len(inputs) < 2:
        return inputs
    pivot = random.choice(inputs)
    left = [ii for ii in inputs if ii < pivot]
    medium = [jj for jj in inputs if jj == pivot]
    right = [kk for kk in inputs if kk > pivot]
    return qsort(left) + medium + qsort(right)

inputs = [2,3,8,4,9,5,6,5,6,10,17,11,2]
outputs = qsort(inputs)
print(outputs)